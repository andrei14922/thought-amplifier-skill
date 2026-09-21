[CmdletBinding()]
param(
    [string]$Destination
)

$ErrorActionPreference = 'Stop'

$packageRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourceSkill = Join-Path $packageRoot '.agents\skills\thought-amplifier'

if (-not $Destination) {
    $Destination = Join-Path ([Environment]::GetFolderPath('UserProfile')) '.agents\skills\thought-amplifier'
}

$sourceSkill = [System.IO.Path]::GetFullPath($sourceSkill)
$destinationSkill = [System.IO.Path]::GetFullPath($Destination)
$destinationParent = Split-Path -Parent $destinationSkill

if (-not (Test-Path -LiteralPath (Join-Path $sourceSkill 'SKILL.md') -PathType Leaf)) {
    throw "The packaged skill is incomplete: SKILL.md was not found."
}

New-Item -ItemType Directory -Path $destinationParent -Force | Out-Null

$backupPath = $null
if (Test-Path -LiteralPath $destinationSkill) {
    $timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $backupPath = "$destinationSkill.backup-$timestamp"
    if (Test-Path -LiteralPath $backupPath) {
        throw "Backup path already exists: $backupPath"
    }
    Move-Item -LiteralPath $destinationSkill -Destination $backupPath
}

try {
    Copy-Item -LiteralPath $sourceSkill -Destination $destinationSkill -Recurse
}
catch {
    if ($backupPath -and -not (Test-Path -LiteralPath $destinationSkill) -and (Test-Path -LiteralPath $backupPath)) {
        Move-Item -LiteralPath $backupPath -Destination $destinationSkill
    }
    throw
}

if (-not (Test-Path -LiteralPath (Join-Path $destinationSkill 'SKILL.md') -PathType Leaf)) {
    throw "Installation verification failed: SKILL.md is missing from the destination."
}

Write-Host "Thought Amplifier installed successfully."
Write-Host "Location: $destinationSkill"
if ($backupPath) {
    Write-Host "Previous version preserved at: $backupPath"
}
Write-Host 'Open a new Codex or ChatGPT session if the skill is not visible immediately.'

