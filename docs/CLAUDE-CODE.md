# Set up Thought Amplifier in Claude Code

**Current edition: 0.3.0 — Public preview.** [Choose a different assistant](../README.md#choose-your-edition).

Claude Code works in the **Code tab of the Claude desktop app**, in a terminal, and in supported code editors. These steps target a **local session on your computer**. If you simply chat at claude.ai or in Claude's everyday conversation view, use the [Claude upload guide](CLAUDE.md) instead.

## Three steps

### 1. Open Claude Code

In the Claude desktop app, open **Code**, choose a **Local** session, and select a project folder. Or open the local Claude Code terminal/editor interface you already use. [Official desktop setup](https://code.claude.com/docs/en/desktop-quickstart).

### 2. Copy and send this installation message

Use the copy icon on GitHub, or select and copy this text. Paste it into Claude Code:

```text
Install the Claude edition of Thought Amplifier from https://github.com/andrei14922/thought-amplifier-skill. Read docs/CLAUDE-CODE.md and copy the complete .claude/skills/thought-amplifier source folder into my personal ~/.claude/skills/thought-amplifier folder. If that skill is already installed or synced from my account, check it first and ask before replacing it or creating a duplicate. Tell me when installation is complete and where it was installed.
```

Allow the download and local file changes if prompted. Wait for completion. The session needs network and filesystem access. A cloud, SSH or WSL session saves files in that environment, so it may not install into your desktop's local profile.

### 3. Try it

Open a fresh Claude Code session and send:

```text
/thought-amplifier ONBOARD THOUGHT AMPLIFIER
```

Then:

```text
/thought-amplifier Amplify this thought: I have too many projects and need to choose what to do this week.
```

## Manual installation

1. [Download the Claude skill ZIP](../downloads/claude/v0.3.0/thought-amplifier-claude-v0.3.0.zip?raw=true) and extract it. On Windows, right-click and choose **Extract All**; on macOS, double-click it.
2. Find the enclosed `thought-amplifier` folder containing `SKILL.md`. Copy that whole folder, including its references. Preserve any existing installation before replacing it.
3. Paste it into your personal skills location below, then open a fresh Claude Code session and try the prompt above.

| Your computer | Where to put the folder |
| --- | --- |
| Windows | Press **Windows + R**, enter `%USERPROFILE%`, and open or create `.claude`, then `skills`. Paste `thought-amplifier` inside. |
| macOS | In Finder, choose **Go → Home**. Press **Command + Shift + .** to show hidden files. Open or create `.claude`, then `skills`, and paste the folder inside. |
| Linux | In your home folder, show hidden files and open or create `.claude/skills`. Paste the folder inside. |

The result should be `~/.claude/skills/thought-amplifier/SKILL.md` with all supporting files. Here `~` means your home folder. Avoid a second nested `thought-amplifier` folder. For project-only use, place the folder inside that project's `.claude/skills` instead of your personal directory.

## If it does not appear

Check the installation path, open a fresh session and type `/thought-amplifier`. Ask Claude Code to check for a personal, project or account-synced skill with the same name. Do not install a second copy if the account version already works. [Official Claude Code skill documentation](https://code.claude.com/docs/en/skills).

## Version and validation

This is the same Claude **0.3.0 public preview** offered for account upload. The public core and references match Codex. Packaging checks passed; fresh Claude behavior and account-upload tests remain pending. [Version and checksum](RELEASES.md#claude-030--public-preview).

To remove a local installation, remove only its `thought-amplifier` folder after checking the path. Restore a preserved version to roll back. [Examples and conversation controls](../README.md#what-it-helps-you-do).
