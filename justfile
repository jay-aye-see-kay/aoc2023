default:
  just --list

check-formatting:
  isort . --check-only
  black . --check

format:
  isort .
  black .

test:
  python -m unittest

download DAY:
  #!/bin/sh
  day="$(printf %02d {{DAY}})"
  mkdir -p inputs
  cd inputs
  aoc download \
    --day "$day" \
    --year 2023 \
    --overwrite \
    --input-file "day-$day.txt" \
    --puzzle-file "day-$day-puzzle.md"
