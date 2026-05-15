#!/usr/bin/env bash
set -euo pipefail

api() {
    local input="${1:-}"
    if [[ -z "$input" ]]; then
        echo "Usage: api <input>"
        return 1
    fi

    echo "Processing api: $input"
    # Validate
    if [[ ! -f "$input" ]]; then
        echo "Error: File not found" >&2
        return 1
    fi

    # Process
    local result=$(sanitize "$input")
    echo "$result"
}

main() {
    api "$@"
}

main "$@"


#!/usr/bin/env bash
set -euo pipefail

model() {
    local input="${1:-}"
    if [[ -z "$input" ]]; then
        echo "Usage: model <input>"
        return 1
    fi

    echo "Processing model: $input"
    # Validate
    if [[ ! -f "$input" ]]; then
        echo "Error: File not found" >&2
        return 1
    fi

    # Process
    local result=$(sanitize "$input")
    echo "$result"
}

main() {
    model "$@"
}

main "$@"


#!/usr/bin/env bash
set -euo pipefail

validator() {
    local input="${1:-}"
    if [[ -z "$input" ]]; then
        echo "Usage: validator <input>"
        return 1
    fi

    echo "Processing validator: $input"
    # Validate
    if [[ ! -f "$input" ]]; then
        echo "Error: File not found" >&2
        return 1
    fi

    # Process
    local result=$(sanitize "$input")
    echo "$result"
}

main() {
    validator "$@"
}

main "$@"
