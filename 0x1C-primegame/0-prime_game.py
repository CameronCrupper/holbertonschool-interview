#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of
consecutive integers starting from 1 up to and
including n, they take turns choosing a prime number
from the set and removing that number and its
multiples from the set. The player that cannot
make a move loses the game.
"""


# def is_prime(x, nums):
#     if nums > 1:
#         for x in range(2, int(num/2)+1):
#             if (nums % x) == 0:
#                 return False
#     return True

def isWinner(x, nums):
    """
    a winner is found at the end
    """
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return "Maria"
    if x == 1:
        return "Maria" if nums[0] == 1 else "Ben"
    n = len(nums)
    for i in range(n):
        if nums[i] in nums[i+1:n]:
            nums.remove(nums[i])
    return isWinner(x-1, nums)
