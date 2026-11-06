# Skill structure and quality

Each skill is an independent folder with a `SKILL.md` file. Its YAML frontmatter contains a lowercase, hyphenated name and a focused description.

## Contents

- Purpose and appropriate use.
- Platform scope and limitations.
- Required context and evidence.
- A task-specific procedure.
- Expected deliverables.
- An illustrative request.

Skills must work without requiring other repository documents. Put substantial supporting material inside the skill's own `references/` folder and link it from `SKILL.md` when needed.

## Writing for developers new to AI

Repository guides must explain unfamiliar terms, show where to place instructions, provide a realistic request, and describe how to assess the answer. Keep this teaching material in user-facing documentation; skill instructions should remain focused on agent behavior.

Use the [request template](request-template.md) for examples. Distinguish an observable symptom from a suspected cause. Preserve exact identifiers supplied by a user, and label synthetic examples clearly.

Maintain repository documentation and skill instructions in English. Users may request answers in other languages. Add content only when it helps someone choose, use, evaluate, or improve a skill.

## Review criteria

- Does not treat O11 and ODC as interchangeable.
- Does not invent actions, APIs, settings, or tools.
- Distinguishes VERIFIED, INFERRED, and UNKNOWN claims with source scope.
- Separates reported context, target identity, and verified tool access.
- Treats embedded instructions in evidence as data, not scope authorization.
- Asks only for material unresolved decisions; blocks only dependent work.
- Verifies authorized writes and separates model checks from runtime tests.
- Provides a practical verification method.
- Does not assume access or credentials.
- Does not grant authorization for unrelated changes or deployments.
- Has a description that distinguishes it from other skills.

The common safety guidance stays inside each skill because users can install
or paste one folder independently. Do not add a mandatory repository-wide
reference or a second gate workflow that duplicates it. Shared wording should
remain short; platform API contracts belong to the official OutSystems skill.

## Maturity

The six starter skills have no comparative agent evaluation yet. Before claiming behavioral validation, record platform, agent/version, scenario, sanitized evidence, observed result, and limitations. Structural checks do not establish correctness of every recommendation.

See [Evaluation](evaluation.md) for executable structural checks and behavioral
cases, and the [audit record](audits/2026-11-06.md) for the evidence behind changes.
