# Thought Amplifier / Amplificatorul de gânduri

**Bring the raw thought. Leave with a clearer question, useful options and a concrete next move.**

## Choose your edition

**Start here. Choose the assistant you already use.** No coding or GitHub account is needed to download the skill or follow the recommended setup. You do need access to your chosen AI app.

[![Set up for Codex](assets/start-codex.svg)](docs/CODEX.md)

For the **OpenAI Codex app**, or Codex in a terminal or code editor. Opens three steps with a message you can copy into Codex. [Manual setup is also available](docs/CODEX.md#manual-installation).

[![Set up for Claude Code](assets/start-claude-code.svg)](docs/CLAUDE-CODE.md)

For the **Code tab in the Claude desktop app**, or Claude Code in a terminal or code editor. Opens three steps with a message you can copy into Claude Code.

[![Download for Claude](assets/download-claude.svg)](downloads/claude/v0.3.0/thought-amplifier-claude-v0.3.0.zip?raw=true)

For **everyday Claude conversations at claude.ai or in the Claude desktop app**, including Cowork. Downloads the ready-to-upload ZIP. **Next: [follow these three upload steps](docs/CLAUDE.md#claude-web-desktop-or-cowork).** Keep the file zipped.

**Not sure which Claude you use?** If you normally open Claude and start chatting, choose **Download for Claude**. If you deliberately open the **Code** tab or use the `claude` terminal command, choose **Set up for Claude Code**. These are different ways to use Claude, not two Thought Amplifier products. The same Claude skill supports both; the setup differs. [See the interface explanation](docs/CLAUDE.md#which-claude-do-i-use).

The setup buttons open instructions. The download button saves a file. **Downloading alone does not install the skill.** You do not need GitHub's green **Code** menu for the recommended routes above.

| Edition | Current version | What you are getting |
| --- | --- | --- |
| Codex | **0.1.0** | Existing public skill; unchanged |
| Claude and Claude Code | **0.3.0 — Public preview** | Same public thinking core; fresh Claude behavior and account-upload tests pending |

[Version history and checksums](docs/RELEASES.md). Version numbers are independent between platforms. Download a new version when you want to update; a local installation does not automatically follow changes to this repository.

**Free skill, MIT license.** There is no separate Thought Amplifier fee. Your AI provider's account requirements, usage limits and charges still apply. Thought Amplifier adds instructions to your existing assistant; it is not a separate application. A Custom GPT is a separate way to use an assistant, not something this repository installs.

![Scattered thoughts become structured decision cards and a clear path forward](assets/thought-amplifier-social-preview.png)

## What it helps you do

Thought Amplifier is a practical thinking skill for **Codex and Claude**, in **English and Romanian**. Bring an idea, question, decision, plan, rough prompt, stuck problem or messy brain dump. You do not need to organize it first.

It is designed to challenge weak assumptions respectfully, organize information without flattening creativity, and help you decide what to do next. It is a thinking partner, not a motivation bot or a yes-man. Results still depend on the model, the context you supply and your judgment.

| Bring this | Get help with | Try this |
| --- | --- | --- |
| A tangled thought | A clearer question, relevant facts and unknowns | `Amplify this thought: [paste whatever is in your head]` |
| A difficult choice | Sharper options, tradeoffs and a conditional recommendation | `COMPARE OPTIONS: [A and B]. Here is what matters to me: [...]` |
| A rough prompt | A stronger prompt with inputs, output format and checks | `PROMPT ARCHITECT: Improve this request for [audience/tool]: [...]` |
| An ambitious goal | A workable plan, dependencies and the first unblocker | `TURN INTO PLAN: [goal, deadline and constraints]` |
| A brainstorming topic | Varied ideas, useful groupings and a next experiment | `BRAINSTORM THIS: [topic]. Give me distinct approaches, then shortlist.` |
| A favorite idea | Respectful challenge, weak assumptions and disconfirming evidence | `PRESSURE TEST: [idea]. What would change the recommendation?` |
| Too many commitments | A clearer priority and explicit tradeoffs | `I have [projects], [time] and [deadlines]. Help me choose what comes first.` |
| A recurring problem | Competing explanations and a small diagnostic test | `Help me diagnose why [problem] keeps happening. Here is the evidence: [...]` |
| Mixed notes or documents | An organized inventory, contradictions, duplicates and supported totals | `Organize these records. Separate facts from assumptions and flag missing information.` |
| Something to learn | Explanation, examples, recall practice and a knowledge check | `Teach me [topic], then ask one question to check my understanding.` |

These are supported workflows, not promises of perfect decisions or verified facts. The assistant should say when evidence is incomplete.

## Your first conversation

After installation, explicitly select the skill once:

**Codex**

```text
$thought-amplifier Amplify this thought: [paste whatever is in your head]
```

**Claude Code**

```text
/thought-amplifier Amplify this thought: [paste whatever is in your head]
```

**Claude web, desktop or Cowork**, with the skill enabled:

```text
Use Thought Amplifier. Amplify this thought: [paste whatever is in your head]
```

“Amplify this thought” is a natural request, not a special command you must memorize. Ordinary requests also work. Explicitly naming the skill helps when automatic selection misses it.

For a guided introduction in Claude, send `Use Thought Amplifier. ONBOARD THOUGHT AMPLIFIER.` In Codex, ask `$thought-amplifier Explain what you do and show me three examples.`

### A small example

> I want to launch a newsletter, build an app and take a course. I have five hours a week, and the newsletter draft is due Friday. Amplify this thought.

A useful response would clarify what matters this week, separate the deadline from optional ambitions, recommend a feasible priority, explain what to defer, and name one next action. It should not simply tell you to work harder. This is an illustration of the intended workflow, not a benchmark result.

### In Romanian

```text
Folosește Thought Amplifier. SCRIE TOT CE AI ÎN MINTE:
Am prea multe proiecte și doar cinci ore disponibile săptămâna aceasta.
Ajută-mă să aleg ce fac mai întâi și ce amân.
```

Both editions follow the language of your request. Override it with `Language: English`, `Language: Română` or `Language: Auto`.

## Control the conversation

- **Only one action:** `NEXT STEP ONLY` / `DOAR URMĂTORUL PAS`.
- **Clarify first:** `Questions first`.
- **Proceed with assumptions:** `No questions`.
- **Choose depth:** `Depth: 30s | 1-minute | normal | deep`.
- **Choose challenge level:** `Strictness: gentle | balanced | ruthless`.
- **Lock the format:** `Output only: <format>` or `Output sections EXACTLY: <headings>`.
- **Keep it offline:** `No browsing` or `Offline`.
- **Keep a continuation note:** `SUMMARIZE FOR LATER` / `REZUMĂ PENTRU MAI TÂRZIU`.
- **Make a repeatable process:** `MAKE THIS REUSABLE` / `FĂ ASTA REUTILIZABIL`.

## What to expect—and what not to assume

- The skill separates facts, interpretations, assumptions and unknowns. It does not make unsupported information true.
- It should challenge an idea respectfully without attacking you or burying a small question in a framework.
- It can help reason about important decisions, but it does not replace qualified professional judgment.
- It does not create permanent memory, grant account access or authorize messages, installations or publication.
- The skill packages contain no connectors, telemetry or executable scripts. The repository's optional Codex installers only copy the Codex skill locally; maintainer tests validate packages.
- Your conversations are handled by the host application's privacy and retention settings.
- Claude **0.3.0 is a public preview**. Its public-source parity and static packaging checks passed; fresh Claude behavior, automatic routing and account upload remain unverified. Equal performance across hosts is not claimed.

## Feedback

Tell us what felt useful, generic, confusing or missing. Include the platform, skill version, a non-sensitive example prompt and what you expected. Do not post private documents, passwords or account details. [Open a GitHub issue](https://github.com/andrei14922/thought-amplifier-skill/issues).

## Source and license

- [Codex skill source](.agents/skills/thought-amplifier/SKILL.md)
- [Claude skill source](.claude/skills/thought-amplifier/SKILL.md)
- [Versions and validation](docs/RELEASES.md)
- [MIT license](LICENSE.md)

The Claude edition preserves the public Codex core and four public references, with Claude-specific discovery metadata and onboarding. Neither distribution includes a private operating-system skill or personal memory.
