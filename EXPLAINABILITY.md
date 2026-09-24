# Quiz Question Quality Auditor Explainability

## Decision and reasoning

The agent decides whether each question passes documented structural checks or needs review. Its reasoning tests prompt presence, option count, normalized duplicate options, answer membership, and configured ambiguity words.

## Inputs and data sources

Inputs are local JSON question records with identifier, prompt, options, and answer. The agent uses no learner data, answer history, or external curriculum source.

## Limits and known constraints

The agent cannot establish factual correctness, instructional value, reading-level suitability, fairness, or alignment with learning outcomes. Absolute wording may be valid in context, so all findings require educator judgment.
