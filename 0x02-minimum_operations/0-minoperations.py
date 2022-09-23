#/usr/bin/python3
"""
Minimum operations
"""

import sys


def minOperations(n):
    """
    calculates fewest number of operations needed to result
    in exactly n H characters in the file
    """
    if n <= 1:
        return 0
    number = n
    divide = 2
    numOfOp = 0

    while number > 1:
        if number % divide == 0:
            number = number / divide
            numOfOp = numOfOp + divide
        else:
            divide += 1

    return numOfOp
