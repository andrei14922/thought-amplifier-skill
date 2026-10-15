# Claude: install and start

**Current edition: 0.3.0 — Public preview.** [Back to the platform chooser](../README.md#choose-your-edition).

[Download thought-amplifier-claude-v0.3.0.zip](../downloads/claude/v0.3.0/thought-amplifier-claude-v0.3.0.zip?raw=true)

This is the dedicated Claude skill ZIP, not GitHub's **Code > Download ZIP** archive of the entire repository. You do not need the Codex edition.

The public reasoning core and all four public method/language references match the Codex edition. Claude has its own discovery description, setup instructions and guided onboarding. Source and packaging checks passed; fresh Claude behavior, routing and account-upload validation remain pending.

## Claude web, desktop or Cowork

1. Download the dedicated ZIP above. Keep it zipped for account upload.
2. Enable **Code execution and file creation** if required in Claude settings. Organization policies may also control skill availability.
3. Open **Customize > Skills > + > Create skill > Upload a skill**.
4. Select the ZIP and enable Thought Amplifier.
5. Start a conversation and send:

```text
Use Thought Amplifier. ONBOARD THOUGHT AMPLIFIER.
```

Then try:

```text
Use Thought Amplifier. Amplify this thought: [paste whatever is in your head]
```

An ordinary chat attachment alone is not a reusable account installation. If an older Thought Amplifier is present, preserve it and use Claude's available replace/remove controls; avoid leaving multiple versions enabled under the same name.

Menu labels and availability can change. [Official Claude setup instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Claude Code

Use the same download, but unzip it. Copy the enclosed `thought-amplifier` folder to one chosen scope:

- **Personal:** `~/.claude/skills/thought-amplifier` for local projects.
- **Project:** `.claude/skills/thought-amplifier` inside the intended project.

The repository also contains the same source folder at [.claude/skills/thought-amplifier](../.claude/skills/thought-amplifier). Copy the whole folder, not just SKILL.md. Preserve a differing installed version before replacement.

Open a fresh Claude Code session in the intended scope and send:

```text
/thought-amplifier ONBOARD THOUGHT AMPLIFIER
```

Then:

```text
/thought-amplifier Amplify this thought: [your situation]
```

If the wrong version runs, check for another personal, project or account-synced skill with the same name. [Official Claude Code skill documentation](https://code.claude.com/docs/en/skills).

## Confirm it works for you

Try a messy decision, a Romanian request, and `Teach me opportunity cost, then ask one question and wait.` Expect useful structure, natural language and an actual knowledge check. For precise or tiny tasks, the skill should not add an unnecessary framework. These are user smoke checks, not a promise of benchmarked results.

You can ask for `NEXT STEP ONLY`, `Questions first`, `No questions` or a specific output format. See the [capability examples](../README.md#what-it-helps-you-do).

## Version, integrity and rollback

The filename identifies the version. [Release information and checksum](RELEASES.md#claude-030--public-preview) identify the exact archive. Compare the SHA-256 if you need to verify a transferred copy.

Disable/remove the skill in Claude settings to stop account use. For a local Claude Code installation, confirm the exact folder before removing it and restore your preserved version to roll back. Do not remove other skills. [Instructions inside the package](../.claude/skills/thought-amplifier/INSTALL-AND-ONBOARD.md) cover the same process.
