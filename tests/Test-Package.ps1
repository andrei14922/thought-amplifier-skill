[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

$repositoryRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$skillRoot = Join-Path $repositoryRoot '.agents\skills\thought-amplifier'
$requiredFiles = @(
    'SKILL.md',
    'agents\openai.yaml',
    'assets\thought-amplifier-avatar.png',
    'references\thinking-methods.md',
    'references\learning-and-practice.md',
    'references\continuity-and-reuse.md',
    'references\romanian-guide.md'
)

foreach ($relativePath in $requiredFiles) {
    $candidate = Join-Path $skillRoot $relativePath
    if (-not (Test-Path -LiteralPath $candidate -PathType Leaf)) {
        throw "Required file missing: $relativePath"
    }
}

$skillText = Get-Content -Raw -LiteralPath (Join-Path $skillRoot 'SKILL.md')
if ($skillText -notmatch '(?m)^name:\s*thought-amplifier\s*$') {
    throw 'SKILL.md has the wrong or missing skill name.'
}
if ($skillText -notmatch 'Language: Română') {
    throw 'Romanian language control is missing.'
}

$openAiText = Get-Content -Raw -LiteralPath (Join-Path $skillRoot 'agents\openai.yaml')
if ($openAiText -notmatch '(?m)^\s*icon_small:\s*"\./assets/thought-amplifier-avatar\.png"\s*$' -or
    $openAiText -notmatch '(?m)^\s*icon_large:\s*"\./assets/thought-amplifier-avatar\.png"\s*$') {
    throw 'Skill UI metadata does not point to the packaged avatar.'
}

$forbiddenPatterns = @(
    'C:\\Users\\',
    '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
    'gh[pousr]_[A-Za-z0-9_]{20,}',
    'github_pat_[A-Za-z0-9_]{20,}',
    'sk-[A-Za-z0-9_-]{20,}',
    '-----BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----'
)

Get-ChildItem -LiteralPath $skillRoot -Recurse -File | ForEach-Object {
    $fileText = Get-Content -Raw -LiteralPath $_.FullName
    foreach ($pattern in $forbiddenPatterns) {
        if ($fileText -match $pattern) {
            throw "Public-boundary check failed in $($_.FullName): $pattern"
        }
    }
}

$systemTempRoot = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath())
$temporaryRoot = [System.IO.Path]::GetFullPath(
    (Join-Path $systemTempRoot ('thought-amplifier-test-' + [guid]::NewGuid().ToString('N')))
)
$testDestination = Join-Path $temporaryRoot '.agents\skills\thought-amplifier'

try {
    & (Join-Path $repositoryRoot 'install.ps1') -Destination $testDestination
    if (-not (Test-Path -LiteralPath (Join-Path $testDestination 'SKILL.md') -PathType Leaf)) {
        throw 'Installer smoke test failed.'
    }
}
finally {
    if (Test-Path -LiteralPath $temporaryRoot) {
        if (-not $temporaryRoot.StartsWith($systemTempRoot, [System.StringComparison]::OrdinalIgnoreCase) -or
            -not (Split-Path -Leaf $temporaryRoot).StartsWith('thought-amplifier-test-')) {
            throw "Refusing to remove an unexpected test path: $temporaryRoot"
        }
        Remove-Item -LiteralPath $temporaryRoot -Recurse -Force
    }
}

Write-Output 'PASS: required files, bilingual controls, public boundary, and installer smoke test.'
