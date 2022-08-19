#!/usr/bin/python3
"""Defines a function"""
import math


def minOperations(n):
    """Returns the minimum number of operations needed to
    copy and paste a string n times"""

    my_list = []
    # even number divisible
    while n % 2 == 0:
        my_list.append(2)
        n = n / 2

    # n became odd
    for i in range(3, int(math.sqrt(n))+1, 2):
        while (n % i == 0):
            my_list.append(int(i))
            n = n / i

    if n > 2:
        my_list.append(int(n))

    return sum(my_list)
