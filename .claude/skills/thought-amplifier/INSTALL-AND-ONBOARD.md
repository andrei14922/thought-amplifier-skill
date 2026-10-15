# Install Thought Amplifier for Claude

Version 0.3.0. One skill supports English and Romanian. This is the Claude adaptation of the public Thought Amplifier skill; no private edition is included.

## Claude web or desktop / Cowork

1. Enable code execution and file creation in your Claude settings if required.
2. Open **Customize > Skills**, choose **+ > Create skill > Upload a skill** (labels may change).
3. Upload the release ZIP containing the `thought-amplifier` folder and enable the skill.
4. Start a conversation and say: **Use Thought Amplifier. ONBOARD THOUGHT AMPLIFIER.**

Attaching the ZIP to an ordinary conversation does not by itself install a reusable account skill. If account or organization settings prevent upload, report that step instead of claiming success.

## Claude Code

Unzip the package. Copy the whole enclosed `thought-amplifier` folder into `~/.claude/skills/` for personal use, or `.claude/skills/` inside a project for that project only. Do not put the ZIP, a doubled folder, or only SKILL.md there.

If a skill already exists at that exact target, compare it first. Preserve a backup and obtain the user's agreement before replacing differing files. An identical copy needs no change. Check for another installed or account-synced skill with the same name if the wrong version activates.

Open a fresh Claude Code session in the intended scope and run:

`/thought-amplifier ONBOARD THOUGHT AMPLIFIER`

## Verify

Confirm the selected scope and skill name. Check that `SKILL.md`, all five reference files, and `LICENSE.md` are present. Try one messy decision and one Romanian prompt. A routine precise coding request should remain concise. Report what actually worked and any remaining setup step.

The assistant should install only this skill when asked. No dependencies, hooks, plugins, connectors, telemetry, account changes or unrelated settings are required by this package.

## Remove or roll back

In Claude account settings, disable or remove only this skill. In Claude Code, after confirming the exact target, remove only its skill folder; restore the preserved version if rolling back. Keep personal modifications safe.

## Official instructions

- https://support.claude.com/en/articles/12512180-use-skills-in-claude
- https://code.claude.com/docs/en/skills

Setup instructions checked on 15 October 2026. Local package validation does not prove account upload or identical behavior across models.
