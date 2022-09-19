#!/usr/bin/python3
"""Defines a function that rotates a 2D matrix"""


def rotate_2d_matrix(matrix):
    """rotates matrix 90 degrees"""

    # transpose matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # reverse row elements
    for row in matrix:
        start = 0
        end = len(row) - 1
        while (start < end):
            temp = row[start]
            row[start] = row[end]
            row[end] = temp
            start += 1
            end -= 1
