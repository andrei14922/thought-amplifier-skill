# Versions and validation

The README is the human entry point; [VERSIONS.json](../VERSIONS.json) is the machine-readable current-version index. Choose by platform, then check the status. Keep versioned downloads immutable; future packages receive new version numbers and the current-version links are updated together.

| Platform | Current version | Source | Distribution | Status |
| --- | --- | --- | --- | --- |
| Codex | 0.1.0 | [.agents/skills/thought-amplifier](../.agents/skills/thought-amplifier) | Existing repository installers / skill installer | Existing public edition |
| Claude | 0.3.0 | [.claude/skills/thought-amplifier](../.claude/skills/thought-amplifier) | [Dedicated upload ZIP](../downloads/claude/v0.3.0/thought-amplifier-claude-v0.3.0.zip?raw=true) | Public preview |

These are platform-specific version lines. Installing Claude 0.3.0 does not upgrade or replace Codex 0.1.0. Updates are explicit; the package contains no self-updater.

## Claude 0.3.0 — Public preview

Prepared 15 October 2026 from public Codex commit `c23c89efe86def98338d38b25f9612ece5d9eeaa`.

- The public core is retained, with newline normalization only.
- All four shared reference files and the MIT license match their public source.
- Adaptations: Claude-sized discovery description, activation boundaries, guided onboarding and setup instructions.
- ZIP contains eight text files; no scripts, connectors, private memory or Codex UI metadata.
- Static package checks and deliberately invalid negative controls passed.
- Fresh Claude model behavior, automatic routing, reference retrieval and web/account upload are **not yet validated**. Equal performance across models is not claimed. Earlier beta test scores are not used as evidence for this release.

Archive SHA-256:

```text
e1d7e917ea609e8da8054f6b06acd99f8840dda56146399031da5b8c15ff0831
```

[Checksum file](../downloads/claude/v0.3.0/SHA256SUMS.txt) · [Public source manifest](../downloads/claude/v0.3.0/SOURCE-MANIFEST.json)

## Codex 0.1.0 — Existing public edition

Originally released 21 September 2026. The skill, four references, UI metadata, assets, existing installer scripts and installation URL are retained unchanged in this dual-platform update.

## Maintainer checks

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File tests/Test-Package.ps1
python tests/validate_dual_package.py
python tests/validate_dual_package.py --self-test
```

The original test validates the Codex files and installs them into a temporary test destination. The cross-platform Python test checks the version index, shared-source parity, release manifest, archive integrity, package file allowlist, documentation links and private-data patterns. Its self-test injects faults in memory; it does not edit package files.

These deterministic tests validate the distribution, not model output quality. Before promoting Claude beyond preview, test it on its intended Claude surface with a fresh conversation, explicit invocation, natural routing, Romanian, learning, mixed records, exact output and coding non-interference cases. Report failures and the tested model/runtime honestly.
