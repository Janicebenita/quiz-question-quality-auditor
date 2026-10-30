# Quiz Question Quality Auditor Explainability

## Decision and reasoning

The agent decides whether each question passes documented structural checks or needs review. Its reasoning tests prompt presence, option count, normalized duplicate options, answer membership, and configured ambiguity words.

## Inputs and data sources

Inputs are local JSON question records with identifier, prompt, options, and answer. The agent uses no learner data, answer history, or external curriculum source.

## Limits and known constraints

The agent cannot establish factual correctness, instructional value, reading-level suitability, fairness, or alignment with learning outcomes. Absolute wording may be valid in context, so all findings require educator judgment.

## Implementation in This Repository

The executable implementation is in `app.py`. Its `audit_question(q)` function checks prompt length, minimum option count, normalized duplicate options, whether the answer exactly appears among the options, and matches the declared `AMBIGUITY` phrases. `run(items)` returns every question's status, issue codes, matched wording, and a structural-audit disclaimer.

`main()` reads `sample_data.json` or another supplied JSON file, and `test_app.py` verifies the implemented rules. The code does not grade learners or alter a learning-management system; each finding maps to a visible rule and question field.

## Outputs and supporting evidence

Each result contains the question identifier, pass/review status, issue codes, and any matched wording. Those exact fields and deterministic rules are the evidence for the audit result.

## Uncertainty and human review

Structural checks cannot establish factual correctness, fairness, or learning-value alignment. An educator must review every flagged question and approve all content changes.
