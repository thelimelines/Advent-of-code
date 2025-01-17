"""Utility functions and classes for calculating distances.

This module provides:
- `calculate_total_distance`: Calculate the absolute summed distance between two sorted
    arrays from a text file.
- `similarity_score`: Calculate the similarity score between two arrays from a text file
- `tests`: Test functions to validate correctness of utility functions.
"""

import logging
from pathlib import Path

from numpy import abs as np_abs
from numpy import loadtxt, sort
from numpy import sum as np_sum

logging.basicConfig(level=logging.INFO)


def calculate_total_distance(file_path: str) -> int:
    """Calculate the absolute summed distance between two arrays from a text file.

    Args:
        file_path (str): Path to the input text file with two columns of numbers.

    Returns:
        int: The calculated absolute summed distance.

    """
    # Load and sort the data into two arrays
    distances = loadtxt(file_path)
    dist1, dist2 = sort(distances[:, 0]), sort(distances[:, 1])

    # Use NumPy vectorized operations for efficiency
    return int(np_sum(np_abs(dist1 - dist2)))


def similarity_score(file_path: str) -> int:
    """Calculate the similarity score between two arrays from a text file.

    Args:
        file_path (str): Path to the input text file with two columns of numbers.

    Returns:
        int: The calculated similarity score.

    """
    # Load data
    distances = loadtxt(file_path)
    dist1, dist2 = distances[:, 0], distances[:, 1]

    # Calculate similarity score
    return int(
        np_sum([value * np_sum(dist2 == value) for value in dist1]),
    )



def tests() -> None:
    """Run tests for utility functions."""
    test_file_path = "Day-1/test_input.txt"  # Path to the test input file

    # Test `calculate_total_distance`
    expected_distance = 11
    distance_result = calculate_total_distance(test_file_path)
    if distance_result != expected_distance:
        msg = f"Distance Test failed: {distance_result} != {expected_distance}"
        raise ValueError(msg)
    logging.info("Distance test passed!")

    # Test `similarity_score`
    expected_similarity = 31
    similarity_result = similarity_score(test_file_path)
    if similarity_result != expected_similarity:
        msg = f"Similarity Test failed: {similarity_result} != {expected_similarity}"
        raise ValueError(msg)
    logging.info("Similarity test passed!")


if __name__ == "__main__":
    # Run tests before executing main logic
    tests()

    # Example usage
    test_file_path = Path("Day-1/Day1-input.txt")
    total_distance = calculate_total_distance(str(test_file_path))
    logging.info("Total distance: %s", total_distance)

    similarity = similarity_score(str(test_file_path))
    logging.info("Total similarity: %s", similarity)
