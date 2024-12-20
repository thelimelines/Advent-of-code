"""Utility functions and classes for reading txt files and processing arrays.

This module provides:
- .
"""

import numpy as np

# Load the data into two seperate arrays
#distances_unsrt = np.loadtxt("Day-1/Day1-input")
distances_unsrt = np.loadtxt("Day-1/test_input.txt")
dist1_unsrt = distances_unsrt[:, 0]
dist2_unsrt = distances_unsrt[:, 1]

# sort low to high
dist1 = np.sort(dist1_unsrt)
dist2 = np.sort(dist2_unsrt)

total_dist = 0
for i in range(len(dist1)):
    total_dist+=dist2[i]-dist1[i]
