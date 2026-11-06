"""Offline repository checks; these do not evaluate agent decisions or MCP behavior."""

import re
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "outsystems-architecture", "outsystems-core", "outsystems-enduser",
    "outsystems-foundation", "outsystems-security", "outsystems-troubleshooting",
}


def read_metadata(text):
    """Parse YAML, rejecting duplicate keys and invalid discovery metadata."""
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    if not match:
        raise ValueError('Missing or unclosed frontmatter')

    class UniqueLoader(yaml.SafeLoader):
        pass

    def unique_mapping(loader, node):
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node)
            if not isinstance(key, str) or key in result:
                raise ValueError('Non-string or duplicate YAML key')
            result[key] = loader.construct_object(value_node)
        return result

    UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                                 unique_mapping)
    try:
        data = yaml.load(match.group(1), Loader=UniqueLoader)
    except yaml.YAMLError as error:
        raise ValueError(str(error)) from error
    if not isinstance(data, dict):
        raise ValueError('Frontmatter must be a mapping')
    for field in ('name', 'description'):
        if not isinstance(data.get(field), str) or not data[field].strip():
            raise ValueError(f'{field} must be a nonempty string')
    if len(data['name']) > 64 or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', data['name']):
        raise ValueError('Invalid skill name')
    if len(data['description']) > 1024:
        raise ValueError('Description exceeds 1024 characters')
    return data


def prose(text):
    """Exclude fenced code; this checker supports the Markdown forms used here."""
    return re.sub(r'^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$', '', text, flags=re.M | re.S)


def anchors(text):
    counts, result = {}, set()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', prose(text), re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = counts.get(slug, 0)
        result.add(f'{slug}-{count}' if count else slug)
        counts[slug] = count + 1
    return result


def link_errors(root, source):
    """Check inline/reference destinations locally; never request external URLs."""
    text = re.sub(r'(`+).*?\1', '', prose(source.read_text(encoding='utf-8')))
    destinations = re.findall(r'\]\(<?([^\s)>]+)>?(?:\s+"[^"]*")?\)', text)
    destinations += re.findall(r'^\s*\[[^\]]+\]:\s*<?([^\s>]+)>?', text, re.M)
    errors = []
    for destination in destinations:
        parts = urlsplit(destination)
        if parts.scheme or parts.netloc:
            continue
        target = (source.parent / unquote(parts.path)).resolve() if parts.path else source.resolve()
        label = f'{source.relative_to(root)}: {destination}'
        if not target.is_relative_to(root.resolve()):
            errors.append(f'{label}: outside package')
        elif not target.exists():
            errors.append(f'{label}: missing target')
        elif parts.fragment and target.suffix == '.md' and unquote(parts.fragment) not in anchors(target.read_text(encoding='utf-8')):
            errors.append(f'{label}: missing anchor')
    return errors


class ValidatorTests(unittest.TestCase):
    def test_reads_real_yaml_strings(self):
        data = read_metadata('---\nname: demo\ndescription: >-\n  Review flows\n  with evidence.\n---\n# Demo\n')
        self.assertEqual(data, {"name": "demo", "description": "Review flows with evidence."})

    def test_rejects_invalid_metadata(self):
        invalid = [
            '# No frontmatter\n',
            '---\nname: demo\n',
            '---\n[unterminated\n---\n',
            '---\n- list\n---\n',
            '---\nname: demo\n---\n',
            '---\nname: demo\nname: another\ndescription: test\n---\n',
            '---\nname: Demo_Name\ndescription: test\n---\n',
            '---\nname: demo\ndescription: true\n---\n',
            '---\nname: demo\ndescription: ""\n---\n',
        ]
        for text in invalid:
            with self.subTest(text=text), self.assertRaises(ValueError):
                read_metadata(text)

    def test_accepts_relative_links_and_ignores_code_and_external_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'target.md').write_text('# Target\n\n## Usage\n', encoding='utf-8')
            source = root / 'README.md'
            source.write_text('[ok](target.md#usage) [web](https://example.invalid/)\n'
                              '```text\n[placeholder](missing.md)\n```\n'
                              '`[sample](not-a-link.md)`\n', encoding='utf-8')
            self.assertEqual(link_errors(root, source), [])

    def test_reports_missing_file_and_anchor(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'target.md').write_text('# Target\n', encoding='utf-8')
            source = root / 'README.md'
            source.write_text('[file](missing.md)\n[anchor](target.md#absent)\n', encoding='utf-8')
            errors = link_errors(root, source)
            self.assertEqual(len(errors), 2)
            self.assertTrue(any('missing.md' in error for error in errors))
            self.assertTrue(any('absent' in error for error in errors))

    def test_reports_escape_from_package(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'SKILL.md'
            source.write_text('[outside](../README.md)\n', encoding='utf-8')
            self.assertTrue(link_errors(root, source))

    def test_checks_reference_links_and_encoded_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'my guide.md').write_text('# Guide\n', encoding='utf-8')
            source = root / 'README.md'
            source.write_text('[guide][g]\n\n[g]: my%20guide.md#guide\n', encoding='utf-8')
            self.assertEqual(link_errors(root, source), [])
            source.write_text('[guide][g]\n\n[g]: missing.md\n', encoding='utf-8')
            self.assertTrue(link_errors(root, source))


class RepositoryTests(unittest.TestCase):
    def test_six_named_skills_are_discoverable(self):
        directories = {p.name for p in (ROOT / 'skills').iterdir() if p.is_dir()}
        self.assertEqual(directories, SKILLS)
        for name in sorted(SKILLS):
            with self.subTest(skill=name):
                path = ROOT / 'skills' / name / 'SKILL.md'
                metadata = read_metadata(path.read_text(encoding='utf-8'))
                self.assertEqual(metadata.get('name'), name)

    def test_relative_documentation_links_resolve(self):
        errors = []
        for path in self.markdown_files():
            errors.extend(link_errors(ROOT, path))
        self.assertEqual(errors, [])

    def test_each_skill_can_be_copied_independently(self):
        errors = []
        for name in sorted(SKILLS):
            root = ROOT / 'skills' / name
            for path in root.rglob('*.md'):
                errors.extend(link_errors(root, path))
        self.assertEqual(errors, [])

    @staticmethod
    def markdown_files():
        return [*ROOT.glob('*.md'), * (ROOT / 'docs').rglob('*.md'),
                * (ROOT / 'examples').rglob('*.md'), * (ROOT / 'skills').rglob('*.md')]


if __name__ == '__main__':
    unittest.main()
