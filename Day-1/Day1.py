"""Utility functions and classes for calculating distances.

This module provides:
- `calculate_total_distance`: Calculate the absolute summed distance between two sorted
    arrays from a text file.
- `test_calculate_total_distance`: Test function to validate the correctness of
    `calculate_total_distance`.
"""

import logging
from pathlib import Path

from numpy import abs as np_abs
from numpy import loadtxt, sort

logging.basicConfig(level=logging.INFO)


def calculate_total_distance(file_path: str) -> int:
    """Calculate the absolute summed distance based on sorted arrays from a text file.

    Args:
        file_path (str): Path to the input text file with two columns of numbers.

    Returns:
        int: The calculated absolute summed distance.

    """
    # Load the data into two separate arrays
    distances_unsrt = loadtxt(file_path)
    dist1_unsrt = distances_unsrt[:, 0]
    dist2_unsrt = distances_unsrt[:, 1]

    # Sort arrays low to high
    dist1 = sort(dist1_unsrt)
    dist2 = sort(dist2_unsrt)

    # Calculate absolute summed distance
    return sum(np_abs(dist2[i] - dist1[i]) for i in range(len(dist1)))


def tests() -> None:
    """Test function for calculate_total_distance."""
    test_file_path = "Day-1/test_input.txt"  # Use the existing test file

    expected_result = 11
    result = calculate_total_distance(test_file_path)
    if result != expected_result:
        msg = f"Test failed: {result} != {expected_result}"
        raise ValueError(msg)
    logging.info("Dist test passed!")

    """Test function for similarity_score."""
    test_file_path = "Day-1/test_input.txt"  # Use the existing test file

    expected_result = 31
    result = similarity_score(test_file_path)
    if result != expected_result:
        msg = f"Test failed: {result} != {expected_result}"
        raise ValueError(msg)
    logging.info("Similarity test passed!")


def similarity_score(file_path: str) -> int:
    """Calculate the similarity score based on sorted arrays from a text file.

    Args:
        file_path (str): Path to the input text file with two columns of numbers.

    Returns:
        int: The calculated similarity score.

    """
    # Load the data into two separate arrays
    distances_unsrt = loadtxt(file_path)
    dist1_unsrt = distances_unsrt[:, 0]
    dist2_unsrt = distances_unsrt[:, 1]

    # Sort arrays low to high
    dist1 = sort(dist1_unsrt)
    dist2 = sort(dist2_unsrt)

    # Calculate absolute summed distance
    similarity = 0
    for val in dist1:
        similarity += val*(dist2 == val).sum()
    return similarity


if __name__ == "__main__":
    # Run test before executing main logic
    tests()

    # Example usage
    test_file_path = Path("Day-1/Day1-input.txt")
    total_distance = calculate_total_distance(str(test_file_path))
    logging.info("Total distance: %s", total_distance)
    similarity = similarity_score(str(test_file_path))
    logging.info("Total similarity: %s", similarity)
