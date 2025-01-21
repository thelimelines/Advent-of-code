"""Day 2 Advent of Code Solution.

This script processes reports to determine how many are safe
based on specific rules about increasing or decreasing levels.
"""

import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

# Constants for the safety rules
MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 3


def is_safe_report(report: list[int]) -> bool:
    """Check if a report is safe based on the rules.

    A report is safe if:
    - All levels are strictly increasing or strictly decreasing.
    - Adjacent levels differ by at least MIN_DIFFERENCE and at most MAX_DIFFERENCE.

    Args:
        report (list[int]): A list of integer levels.

    Returns:
        bool: True if the report is safe, False otherwise.

    """
    # Check if the report is strictly increasing
    if all(i < j for i, j in zip(report, report[1:])):
        return all(
            MIN_DIFFERENCE <= j - i <= MAX_DIFFERENCE
            for i, j in zip(report, report[1:])
        )
    # Check if the report is strictly decreasing
    if all(i > j for i, j in zip(report, report[1:])):
        return all(
            -MAX_DIFFERENCE <= j - i <= -MIN_DIFFERENCE
            for i, j in zip(report, report[1:])
        )
    # Report is neither increasing nor decreasing
    return False


def count_safe_reports(file_path: Path) -> int:
    """Count the number of safe reports in the input file.

    Args:
        file_path (Path): Path to the input file.

    Returns:
        int: Number of safe reports.

    """
    safe_cnt = 0
    with file_path.open() as file:
        for line in file:
            report = [int(x) for x in line.split()]  # Parse as a list of integers
            if is_safe_report(report):
                safe_cnt += 1
    return safe_cnt


def safe_problem_dampened(file_path: Path) -> int:
    """Count the number of safe reports in the input file when any 1 value may be removed (problem dampener).

    Args:
        file_path (Path): Path to the input file.

    Returns:
        int: Number of safe reports.

    """
    safe_cnt = 0
    with file_path.open() as file:
        for line in file:
            report = [int(x) for x in line.split()]  # Parse as a list of integers
            if is_safe_report(report):
                safe_cnt += 1
            else:
                for i in range(len(report)):
                    temp_report = (
                        report[:i] + report[i + 1 :]
                    )  # Create a copy excluding the i-th element
                    if is_safe_report(temp_report):
                        safe_cnt += 1
                        break
    return safe_cnt


def tests() -> None:
    """Test the algorithm with a sample input file and validate the output."""
    test_file_path = Path("Day-2/test_input.txt")
    expected_safe_count = 2  # Expected result for the test input
    result = count_safe_reports(test_file_path)
    if result == expected_safe_count:
        logging.info("Test passed!")
    else:
        logging.error(
            "Test failed! Expected %s, but got %s.",
            expected_safe_count,
            result,
        )

    expected_safe_count = 4  # Expected result for the test input
    result = safe_problem_dampened(test_file_path)
    if result == expected_safe_count:
        logging.info("Test passed!")
    else:
        logging.error(
            "Test failed! Expected %s, but got %s.",
            expected_safe_count,
            result,
        )


if __name__ == "__main__":
    # Uncomment the line below to test the function
    tests()

    # Count safe reports for the actual input file
    input_file_path = Path("Day-2/Day2_input.txt")
    safe_reports = count_safe_reports(input_file_path)
    logging.info("Number of safe reports: %s", safe_reports)
    safe_dampened_reports = safe_problem_dampened(input_file_path)
    logging.info(
        "Number of safe reports with problem dampener: %s", safe_dampened_reports
    )
