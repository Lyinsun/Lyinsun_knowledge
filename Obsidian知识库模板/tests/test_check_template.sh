#!/usr/bin/env bash
set -euo pipefail

template_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$template_root/scripts/check_template.py" --root "$template_root"
