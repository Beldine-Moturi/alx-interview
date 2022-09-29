#!/usr/bin/python3
"""This module describes a solution to the N Queens problem"""
import sys


def draw_sol(board):
    """draws a solution on the board"""
    solution = []
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                solution.append([i, j])
    return solution


def is_safe(board, row, col):
    """Check if it is *safe to place queen
    in this position of the board"""

    # check column for attacks
    for i in range(row):
        if board[i][col] == 1:
            return False

    # check first diagonal
    (i, j) = (row, col)
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1

    # check second diagonal
    (i, j) = (row, col)
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j + 1

    # return true if no attacks
    return True


def place_queen(board, row):
    """Places a queen at a particular position of the board
    depending on whether it is safe to place it there
    -- prints the solutions"""

    if row >= len(board):
        print(draw_sol(board))
        return

    for i in range(len(board)):
        if is_safe(board, row, i):
            board[row][i] = 1
            place_queen(board, row + 1)
            board[row][i] = 0


if __name__ == "__main__":
    # Get the size of the board from the command line
    args = sys.argv
    if len(args) < 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not args[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(args[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # define/draw the board
    board = [[0 for j in range(n)] for i in range(n)]

    # run the function to find an print all possible solutions

    place_queen(board, 0)
