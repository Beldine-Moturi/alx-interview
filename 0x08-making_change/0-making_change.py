#!/usr/bin/python3
"""Defines the makeChange function"""


def makeChange(coins, total):
    """ the fewest number of coins needed to meet
    the total"""

    if total <= 0:
        return 0

    my_coins = reversed(sorted(coins))
    count = 0
    sum = 0

    for coin in my_coins:
        while sum < total:
            if (sum + coin) > total:
                break
            else:
                sum += coin
                count += 1
                #print(count)
        if sum == total:
            return count

    return -1
