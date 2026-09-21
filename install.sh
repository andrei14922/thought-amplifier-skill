#!/usr/bin/env sh
set -eu

package_root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
source_skill="$package_root/.agents/skills/thought-amplifier"
destination_skill=${1:-"${HOME}/.agents/skills/thought-amplifier"}
destination_parent=$(dirname -- "$destination_skill")

if [ ! -f "$source_skill/SKILL.md" ]; then
  echo "The packaged skill is incomplete: SKILL.md was not found." >&2
  exit 1
fi

mkdir -p "$destination_parent"

backup_path=""
if [ -e "$destination_skill" ]; then
  timestamp=$(date +%Y%m%d-%H%M%S)
  backup_path="$destination_skill.backup-$timestamp"
  if [ -e "$backup_path" ]; then
    echo "Backup path already exists: $backup_path" >&2
    exit 1
  fi
  mv "$destination_skill" "$backup_path"
fi

if ! cp -R "$source_skill" "$destination_skill"; then
  if [ -n "$backup_path" ] && [ ! -e "$destination_skill" ] && [ -e "$backup_path" ]; then
    mv "$backup_path" "$destination_skill"
  fi
  exit 1
fi

if [ ! -f "$destination_skill/SKILL.md" ]; then
  echo "Installation verification failed: SKILL.md is missing from the destination." >&2
  exit 1
fi

echo "Thought Amplifier installed successfully."
echo "Location: $destination_skill"
if [ -n "$backup_path" ]; then
  echo "Previous version preserved at: $backup_path"
fi
echo "Open a new Codex or ChatGPT session if the skill is not visible immediately."

