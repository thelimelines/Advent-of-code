"""Day 3 Advent of Code Solution."""

import logging
import re
from pathlib import Path

logging.basicConfig(level=logging.INFO)

# Pattern for Part 1: match mul(x,y) with x,y up to 3 digits
PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)"
FILE_PATH = Path("Day-3/Day3_input.txt")


def calc_mul_sum(file_path: Path, pattern: str) -> int:
    """Return the sum of products for each mul(x,y) in the file."""
    with file_path.open() as f:
        data = f.read()
    matches = re.findall(pattern, data)
    return sum(int(x) * int(y) for x, y in matches)


def test_calc_mul_sum() -> None:
    """Checks calc_mul_sum against known data."""
    test_file = Path("Day-3/test_input.txt")
    expected = 161
    actual = calc_mul_sum(test_file, PATTERN)
    if actual != expected:
        msg = f"Test failed: {actual} != {expected}"
        raise ValueError(msg)
    logging.info("Test passed: %s == %s", actual, expected)


# Pattern for Part 2: do(), don't(), or mul(...)
PART2_PATTERN = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"


def calc_conditional_mul_sum(file_path: Path, pattern: str) -> int:
    """Return the sum of mul(x,y) products only when enabled by do() or disabled by don't())."""
    with file_path.open() as f:
        data = f.read()

    tokens = re.findall(pattern, data)
    enabled = True
    total = 0

    for full, a, b in tokens:
        if full == "do()":
            enabled = True
        elif full == "don't()":
            enabled = False
        elif enabled:  # mul(...)
            total += int(a) * int(b)

    return total


def test_calc_conditional_mul_sum() -> None:
    """Checks calc_conditional_mul_sum against known data."""
    test_file = Path("Day-3/test_input_2.txt")
    expected = 48
    actual = calc_conditional_mul_sum(test_file, PART2_PATTERN)
    if actual != expected:
        msg = f"Test failed: {actual} != {expected}"
        raise ValueError(msg)
    logging.info("Test passed: %s == %s", actual, expected)


if __name__ == "__main__":
    # Run and log Part 1 test and solution
    test_calc_mul_sum()
    result1 = calc_mul_sum(FILE_PATH, PATTERN)
    logging.info("Part 1 Result: %s", result1)

    # Run and log Part 2 test and solution
    test_calc_conditional_mul_sum()
    result2 = calc_conditional_mul_sum(FILE_PATH, PART2_PATTERN)
    logging.info("Part 2 Result: %s", result2)
