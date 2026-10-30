# Quiz Question Quality Auditor Explainability

## Decision and reasoning

The agent decides whether each question passes documented structural checks or needs review. Its reasoning tests prompt presence, option count, normalized duplicate options, answer membership, and configured ambiguity words.

## Inputs and data sources

Inputs are local JSON question records with identifier, prompt, options, and answer. The agent uses no learner data, answer history, or external curriculum source.

## Limits and known constraints

The agent cannot establish factual correctness, instructional value, reading-level suitability, fairness, or alignment with learning outcomes. Absolute wording may be valid in context, so all findings require educator judgment.

## Implementation in This Repository

`app.py` loads local question records and applies deterministic structural checks to prompts, options, and answer keys. The bundled sample data makes the audit reproducible, and `test_app.py` verifies the implemented checks and report format.

The code does not grade learners or alter a learning-management system. Each finding maps to a visible rule and question field, and an educator must decide whether the item is factually and pedagogically appropriate.
