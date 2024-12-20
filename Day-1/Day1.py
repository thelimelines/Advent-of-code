"""Utility functions and classes for reading txt files and processing arrays.

This module provides:
- Functions for reading and processing numerical data from text files.
"""

import numpy as np


def calculate_total_distance(file_path: str) -> int:
    """Calculate the absolute summed distance based on sorted arrays from a text file.

    Args:
        file_path (str): Path to the input text file with two columns of numbers.

    Returns:
        int: The calculated absolute summed distance.

    """
    # Load the data into two separate arrays
    distances_unsrt = np.loadtxt(file_path)
    dist1_unsrt = distances_unsrt[:, 0]
    dist2_unsrt = distances_unsrt[:, 1]

    # Sort arrays low to high
    dist1 = np.sort(dist1_unsrt)
    dist2 = np.sort(dist2_unsrt)

    # Calculate absolute summed distance
    return sum(abs(dist2[i] - dist1[i]) for i in range(len(dist1)))


if __name__ == "__main__":
    # Example usage
    # test_file_path = "Day-1/test_input.txt"
    test_file_path = "Day-1/Day1-input.txt"
    total_distance = calculate_total_distance(test_file_path)
    print(f"Total distance: {total_distance}")
