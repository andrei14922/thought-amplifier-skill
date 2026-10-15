# Codex: install and start

**Current edition: 0.1.0.** Its source, existing installers and installation URL are unchanged. [Back to the platform chooser](../README.md#choose-your-edition).

## Fastest installation

Paste this into Codex and approve the normal local installation:

```text
$skill-installer Install the skill from https://github.com/andrei14922/thought-amplifier-skill/tree/main/.agents/skills/thought-amplifier
```

Open a new conversation if the skill does not appear immediately. Then try:

```text
$thought-amplifier Amplify this thought: I have too many projects and need to choose what to do this week.
```

## Install from a downloaded repository

Download or clone the repository, extract it if necessary, and open a terminal in its root.

Windows PowerShell:

```powershell
.\install.ps1
```

macOS or Linux:

```sh
sh ./install.sh
```

The installers copy only `.agents/skills/thought-amplifier` to `~/.agents/skills/thought-amplifier` and preserve an existing target in a timestamped backup. They do not install the Claude edition. Review any local edits before replacing an older installation.

For manual installation, copy the entire [.agents/skills/thought-amplifier](../.agents/skills/thought-amplifier) folder to `~/.agents/skills/thought-amplifier`. On Windows, `~` is your user profile. Preserve an existing version before replacing it.

## First-use check

1. Confirm Thought Amplifier is available in a fresh session.
2. Invoke `$thought-amplifier` with a real decision or brain dump.
3. Try a Romanian request or set `Language: Română`.
4. Try `NEXT STEP ONLY`; expect one concrete action.

If it is absent, check the folder contains `SKILL.md`, its references, UI metadata and icon, and that it is not nested inside a second `thought-amplifier` folder. It is a skill inside the host application, not a separate app window. See the [main examples](../README.md#what-it-helps-you-do).

## Update or remove

Check the [current-version table](RELEASES.md) before updating. The repository installers preserve the old version, but a different installation tool may have its own replacement behavior.

To remove a manual/local installation, remove only the exact installed Thought Amplifier folder after checking its path. Restore your preserved folder to roll back. Do not remove neighboring skills.
