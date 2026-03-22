#!/bin/bash
# Запускает main.py из той же папки, что и скрипт
DIR="$(dirname "$0")"
python3 "$DIR/gh.py" "$@"