#!/usr/bin/env bash
set -euo pipefail

kb_root="${1:-.}"
architecture_root="$kb_root/architecture"
topic_map="$kb_root/_index/topic-map.md"
architecture_index="$architecture_root/README.md"
errors=0

report_error() {
  echo "ERROR: $*" >&2
  errors=$((errors + 1))
}

if [[ ! -d "$architecture_root" ]]; then
  report_error "missing architecture directory: $architecture_root"
fi

if [[ ! -f "$architecture_index" ]]; then
  report_error "missing architecture scope index: $architecture_index"
fi

if [[ ! -f "$topic_map" ]]; then
  report_error "missing global topic map: $topic_map"
fi

if [[ -d "$architecture_root" ]]; then
  while IFS= read -r root_page; do
    page_name="$(basename "$root_page")"
    case "$page_name" in
      README.md|overview.md) ;;
      *) report_error "architecture root page is not allowed: $root_page" ;;
    esac
  done < <(find "$architecture_root" -maxdepth 1 -type f -name '*.md' -print | sort)

  while IFS= read -r scope_dir; do
    scope_name="$(basename "$scope_dir")"
    scope_readme="$scope_dir/README.md"

    if [[ ! "$scope_name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
      report_error "architecture scope is not lowercase kebab-case: $scope_dir"
    fi

    if [[ ! -f "$scope_readme" ]]; then
      report_error "architecture scope is missing README.md: $scope_dir"
      continue
    fi

    if [[ -f "$architecture_index" ]] && ! grep -Fq "$scope_name/" "$architecture_index"; then
      report_error "architecture scope is not listed in architecture/README.md: $scope_name"
    fi

    if [[ -f "$topic_map" ]] && ! grep -Fq "architecture/$scope_name/" "$topic_map"; then
      report_error "architecture scope is not grouped in _index/topic-map.md: $scope_name"
    fi

    while IFS= read -r page; do
      page_name="$(basename "$page")"
      [[ "$page_name" == "README.md" ]] && continue

      relative_to_scope="${page#"$scope_dir/"}"
      relative_to_architecture="${page#"$architecture_root/"}"

      if ! grep -Fq "$relative_to_scope" "$scope_readme"; then
        report_error "architecture page is not linked from scope README: $relative_to_architecture"
      fi

      if [[ -f "$topic_map" ]] && ! grep -Fq "architecture/$relative_to_architecture" "$topic_map"; then
        report_error "architecture page is not linked from _index/topic-map.md: $relative_to_architecture"
      fi
    done < <(find "$scope_dir" -type f -name '*.md' -print | sort)
  done < <(find "$architecture_root" -mindepth 1 -maxdepth 1 -type d -print | sort)
fi

if (( errors > 0 )); then
  echo "architecture layout check failed with $errors error(s)" >&2
  exit 1
fi

echo "architecture layout check passed"
