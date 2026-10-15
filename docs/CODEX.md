# Set up Thought Amplifier in Codex

**Current edition: 0.1.0.** [Choose a different assistant](../README.md#choose-your-edition).

Use this guide in the OpenAI Codex app, or a local Codex session in a terminal or code editor. You only need to copy a message; you do not need to write code. The session needs network access and permission to save skill files on your computer. A remote session installs into that remote environment.

## Three steps

### 1. Open Codex

Start a conversation in the Codex app or the Codex interface you already use.

### 2. Copy and send this installation message

Use the copy icon on the message block on GitHub, or select the text and copy it. Paste it into Codex and send it:

```text
$skill-installer Install Thought Amplifier from https://github.com/andrei14922/thought-amplifier-skill/tree/main/.agents/skills/thought-amplifier. Keep all supporting files. If I already have it, ask before replacing it. Tell me when installation is complete and where it was installed.
```

Allow the requested download and local installation if prompted. Wait for Codex to confirm completion. Giving it the link starts a request; it is not proof that installation succeeded.

### 3. Try your first thought

Start a new conversation if the skill is not visible yet. Send:

```text
$thought-amplifier Amplify this thought: I have too many projects and need to choose what to do this week.
```

You are ready when Codex can find the skill and respond to your thought. For an introduction, ask `$thought-amplifier Explain what you do and show me three examples.`

## Manual installation

Use this alternative if you prefer copying files yourself. No installer program is required.

1. [Download the repository ZIP](https://github.com/andrei14922/thought-amplifier-skill/archive/refs/heads/main.zip), then extract it. On Windows, right-click the downloaded ZIP and choose **Extract All**. On macOS, double-click it. Open the extracted `thought-amplifier-skill-main` folder.
2. Inside it, open `.agents`, then `skills`. Copy the entire `thought-amplifier` folder. If dot folders are hidden, enable hidden files in your file manager; on macOS press **Command + Shift + .**.
3. Paste that folder into your personal skills location below. Create `.agents` and then `skills` if absent. Preserve any existing `thought-amplifier` folder before replacing it. Open a fresh Codex session and try the prompt above.

| Your computer | Where to put the folder |
| --- | --- |
| Windows | Press **Windows + R**, enter `%USERPROFILE%`, and open or create `.agents`, then `skills`. Paste `thought-amplifier` inside. |
| macOS | In Finder, choose **Go → Home**, show hidden files, and open or create `.agents`, then `skills`. Paste `thought-amplifier` inside. |
| Linux | In your home folder, show hidden files and open or create `.agents/skills`. Paste `thought-amplifier` inside. |

The result should be `~/.agents/skills/thought-amplifier/SKILL.md`, with the other supplied files beside it. Here `~` means your home folder. Do not copy the outer repository folder into `skills`.

### Optional terminal installers

If you are comfortable with a terminal, open one in the extracted repository folder and use the existing installer instead of the manual copy:

Windows PowerShell:

```powershell
.\install.ps1
```

macOS or Linux:

```sh
sh ./install.sh
```

These unchanged installers copy only the Codex edition to `~/.agents/skills/thought-amplifier` and preserve an existing target in a timestamped backup. If your computer blocks a script, use the manual copy steps above.

## If it does not appear

Open a fresh session. Confirm `SKILL.md` is directly inside the installed `thought-amplifier` folder, with its references and supporting files; avoid a second nested folder of the same name. You can ask Codex to check the installation path. [Official skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Update or remove

Check the [current-version table](RELEASES.md) before updating. Preserve a customized installed version before replacement. To remove a local installation, remove only its `thought-amplifier` folder; restore your preserved folder to roll back. [Examples and conversation controls](../README.md#what-it-helps-you-do).
