# Set up Thought Amplifier in Claude

**Current edition: 0.3.0 — Public preview.** [Choose a different assistant](../README.md#choose-your-edition).

For everyday conversations at **claude.ai** or in the **Claude desktop app**, including Cowork. You do not need Claude Code or a terminal for this route.

## Claude web, desktop or Cowork

### 1. Download the skill

[![Download for Claude](../assets/download-claude.svg)](../downloads/claude/v0.3.0/thought-amplifier-claude-v0.3.0.zip?raw=true)

Your browser saves `thought-amplifier-claude-v0.3.0.zip`, usually in **Downloads**. Keep it zipped. Use this button rather than GitHub's **Code > Download ZIP**, which contains the whole repository.

### 2. Upload it in Claude

Open Claude and go to **Customize → Skills → + → Create skill → Upload a skill**. Select the ZIP from Downloads, then enable Thought Amplifier in your skills list.

If Skills is missing, check **Settings → Capabilities → Code execution and file creation**. Your organization may control availability. Menu labels can vary; [Claude's current upload instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude) show the supported route. Attaching the ZIP to an ordinary chat does not install an account skill.

### 3. Start using it

Start a conversation and send:

```text
Use Thought Amplifier. ONBOARD THOUGHT AMPLIFIER.
```

Then bring a real thought:

```text
Use Thought Amplifier. Amplify this thought: I have too many projects and need to choose what to do this week.
```

You are ready when Thought Amplifier appears enabled in Skills and you can use it in a conversation.

## Which Claude do I use

**Claude** is Anthropic's assistant. You can use it in several interfaces:

| What you use | Which setup to choose |
| --- | --- |
| Conversations at claude.ai or in the Claude desktop app | Use the three upload steps above. |
| Cowork for tasks involving files and tools | Use the same account skill upload. Some accounts now combine chat and Cowork into one conversation experience. |
| The **Code** tab in the Claude desktop app, or Claude Code in a terminal/code editor | Follow the [Claude Code guide](CLAUDE-CODE.md). |

Claude Code is a coding and project-work interface that can work with files and run tools. **It has a graphical desktop interface; a command line is optional.** It uses Claude, but its local skill setup differs from uploading a skill to your Claude account. [Official desktop guide](https://code.claude.com/docs/en/desktop-quickstart). [Chat and Cowork interface changes](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude).

You do not need to install both routes. On supported recent Claude Code versions, account skills can also sync when you sign in with the same Claude account. If Thought Amplifier already appears there, avoid installing a second copy with the same name.

## Claude Code

[Open the separate Claude Code setup guide](CLAUDE-CODE.md) for its three steps and manual alternative.

## If something goes wrong

- **No ZIP in Downloads:** open your browser's downloads list and look for `thought-amplifier-claude-v0.3.0.zip`.
- **Upload rejects the file:** check you selected the dedicated skill ZIP, not the whole repository archive or an extracted folder.
- **Claude is not using it:** confirm the skill is enabled, then explicitly say `Use Thought Amplifier`.
- **You already have an older version:** preserve it before replacing it and avoid leaving duplicate versions enabled.

## Version and validation

The public thinking core and four references match the Codex edition. Packaging checks passed; fresh Claude behavior and account-upload tests remain pending. This is a **public preview**, not a claim of identical results across models. [Version and checksum](RELEASES.md#claude-030--public-preview).

To stop using it, disable or remove it through Claude's Skills controls. [Examples and conversation controls](../README.md#what-it-helps-you-do).
