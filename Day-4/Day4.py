"""Day 4 Advent of Code Solution.

This script solves an nxm wordsearch, looking for the word XMAS in any of the 8 cardinal
direcitons.
"""

import logging
from pathlib import Path

def wordsearch_solve(FILEPATH,WORD):


def test() -> None:
    """Checks calc_mul_sum against known data."""
    test_file = Path("Day-3/test_input.txt")
    expected = 18
    actual = wordsearch_solve(test_file, "XMAS")
    if actual != expected:
        msg = f"Test failed: {actual} != {expected}"
        raise ValueError(msg)
    logging.info("Test passed: %s == %s", actual, expected)

if __name__ == "__main__":
    # Run and log Part 1 test and solution
    test()