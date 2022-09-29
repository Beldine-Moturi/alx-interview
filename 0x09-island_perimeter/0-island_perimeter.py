#!/usr/bin/python3
"""Solves the Island perimeter problem"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                above = grid[i - 1][j] if i else 0
                below = grid[i + 1][j] if i < len(grid) else 0
                right = grid[i][j + 1] if j < len(grid[i]) else 0
                left = grid[i][j - 1] if j else 0

                if not above:
                    perimeter += 1
                if not below:
                    perimeter += 1
                if not right:
                    perimeter += 1
                if not left:
                    perimeter += 1

    return perimeter
