# Thinking Methods

Choose one to three methods that fit the request. Do not expose method names unless the user asks or enables `Show techniques: on`.

## Clarify a Messy Thought

Return a clearer question, likely intent, success criteria, knowns and unknowns, hidden assumptions, possible routes, and the strongest next move.

## Analyze and Recommend

1. State success and constraints.
2. Generate three to five plausible approaches.
3. Compare impact, effort, risk, dependencies, and reversibility.
4. Recommend one approach.
5. Name the main risks and mitigations.
6. Give the smallest useful test and next actions.

## Compare Options

Define the criteria first, separate must-haves from preferences, compare the options consistently, identify the decisive tradeoff, and give a conditional recommendation. Avoid fake numerical precision.

## Pressure Test

Return the strongest version of the idea, its weakest link, plausible failure modes, evidence that would change the conclusion, and a better next test.

## Find Blind Spots

Check assumptions, constraints, stakeholders, evidence, incentives, and whether the problem is framed correctly.

## Diverge, Cluster, Converge

Generate raw ideas, cluster them by theme, shortlist the strongest candidates, and choose one next experiment.

## Planning

- **Define Done:** write success criteria and an out-of-scope list.
- **Backward Planning:** start from the outcome and work backward through the necessary milestones.
- **Dependency Map:** identify tasks, dependencies, the critical sequence, and the first unblocker.
- **MVP First:** find the smallest version that creates learning or value.
- **Next Step Only:** give one concrete action with minimal context.

## Diagnose a Failure

- **5 Whys:** follow the symptom toward a deeper cause.
- **Is / Is Not:** compare where, when, who, or what is affected versus unaffected.
- **Evidence Matrix:** list competing explanations and the evidence for and against each.
- **Falsification Focus:** ask what would disprove the favored explanation and which test is cheapest.

## Premortem

Imagine the plan failed. Ask why, what can be mitigated now, and what signal should trigger a change of course.

## Systems View

Clarify purpose, scope, constraints, inputs, outputs, controls, disturbances, feedback, and success or failure criteria.

For design problems, trace:

`desired effect -> required function -> responsible component`

Look for desired effects without functions, functions without owners, and components that do not contribute to the outcome.

## Prompt Architect

1. Define the objective and target user or runtime.
2. Separate governing instructions from source material and examples.
3. Define the expected input, output contract, and success criteria.
4. Add constraints, failure modes, and quality checks.
5. Include an example or small test when useful.
