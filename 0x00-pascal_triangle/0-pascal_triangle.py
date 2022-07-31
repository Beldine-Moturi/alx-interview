#!/usr/bin/python3
"""
Defines a function  pascal_triangle that returns a list of lists of
integers representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n
    Assuming n will always be an integer"""

    if n > 0:
        array = [[1], [1, 1]]
        if n <= 2:
            return array[:n]
        for x in range(2, n):
            arr = [1, ]
            temp = array[x - 1]
            i = 0
            while (i < len(temp) - 1):
                n = temp[i] + temp[i + 1]
                arr.append(n)
                i += 1
            arr.append(1)
            array.append(arr)
        return array
    return []
