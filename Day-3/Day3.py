"""Day 3 Advent of Code Solution."""

import logging
import re
from pathlib import Path

logging.basicConfig(level=logging.INFO)

# Pattern with capturing groups to extract numbers
PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)"

# Path to the input file
#FILE_PATH = Path("Day-3/test_input.txt")
FILE_PATH = Path("Day-3/Day3_input.txt")
def strip_mul_and_apply(file_path: Path, pattern: str) -> int:
    """Calculate the sum of products of numbers extracted from a file in format 'mul(XXX,XXX)."""
    with file_path.open(encoding="utf-8") as file:
        content = file.read()
    matches = re.findall(pattern, content)
    logging.info("Matches found: %s", matches)
    return sum(int(a) * int(b) for a, b in matches)

if __name__ == "__main__":
    result = strip_mul_and_apply(FILE_PATH, PATTERN)
    logging.info("Number: %s", result)
