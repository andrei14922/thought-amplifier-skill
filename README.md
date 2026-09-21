# Thought Amplifier / Amplificatorul de gânduri

![Thought Amplifier turns scattered thoughts into structured decision cards and a clear path forward](assets/thought-amplifier-social-preview.png)

Turn brain dumps, vague questions, overloaded decisions, stuck plans, and rough prompts into clearer thinking and practical next steps.

This repository contains one bilingual Codex/ChatGPT skill. It automatically mirrors English or Romanian, and users can override the language at any time.

## What it does

- clarifies the real question;
- separates facts, assumptions, unknowns, and competing interpretations;
- compares options and recommends a next move;
- turns brain dumps into an organized plan;
- pressure-tests ideas without being hostile;
- improves prompts, specifications, and repeatable workflows;
- helps users learn through explanation and practice.

The package adds no separate account, API key, external service, MCP server, or telemetry.

## Install

### Codex — fastest

Open Codex, paste this, and approve the normal local skill installation:

```text
$skill-installer Install the skill from https://github.com/andrei14922/thought-amplifier-skill/tree/main/.agents/skills/thought-amplifier
```

Then start a new conversation and use:

```text
$thought-amplifier Help me turn this brain dump into a clear decision and next steps: [paste anything]
```

The skill includes a display name, icon, default prompt, and automatic English/Romanian behavior. It appears as a skill inside supported Codex/ChatGPT clients; it is not a separate desktop application with its own window.

### Windows — easiest

Download or clone this repository, open PowerShell in its folder, and run:

```powershell
.\install.ps1
```

The installer copies the skill to:

```text
%USERPROFILE%\.agents\skills\thought-amplifier
```

If an older copy exists, it is preserved in a timestamped backup beside the installed skill.

### macOS or Linux

```bash
./install.sh
```

### Manual installation

Copy this folder:

```text
.agents/skills/thought-amplifier
```

to:

```text
~/.agents/skills/thought-amplifier
```

Restart or open a new Codex/ChatGPT session if the skill does not appear immediately.

## Use

Invoke the skill explicitly:

```text
$thought-amplifier I have too many projects and cannot tell what to do first.
```

Or use one of the natural controls:

```text
BRAIN DUMP: [paste everything]
ANALYZE & RECOMMEND: [situation]
COMPARE OPTIONS: [A vs B]
PRESSURE TEST: [idea]
TURN INTO PLAN: [rough goal]
PROMPT ARCHITECT: [rough request]
NEXT STEP ONLY: [situation]
```

Romanian examples:

```text
$thought-amplifier Nu mai știu ce să prioritizez. Ajută-mă să pun ordine.
SCRIE TOT CE AI ÎN MINTE: [lipește ideile]
ANALIZEAZĂ ȘI RECOMANDĂ: [situația]
COMPARĂ OPȚIUNILE: [A și B]
TRANSFORMĂ ÎN PLAN: [obiectiv]
```

## Language

The default is `Language: Auto`: the answer follows the user's language. Override it with:

```text
Language: English
Language: Română
Language: Auto
```

There is no separate Romanian installation and no setup wizard to maintain. One installation supports both languages.

## Privacy

This repository contains the skill, its supporting references, UI metadata, installers, tests, licence, and media assets. It contains no credentials, personal data, local machine paths, bundled connectors, or telemetry code.

The skill includes no network or storage code. Material pasted into a conversation is handled by the host application under that application's privacy and retention settings.

## Licence

Released under the MIT License. See [LICENSE.md](LICENSE.md).

## Media

- Repository hero: `assets/thought-amplifier-social-preview.png`
- GitHub social preview: `assets/thought-amplifier-github-social-preview.jpg` (1280×640, under 1 MB)
- Public profile/avatar export: `assets/thought-amplifier-github-avatar.jpg` (512×512, under 1 MB)
- Lossless avatar source: `assets/thought-amplifier-avatar.png`
