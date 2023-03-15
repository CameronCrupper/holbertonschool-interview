#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of
consecutive integers starting from 1 up to and
including n, they take turns choosing a prime
number from the set and removing that number
and its multiples from the set. The player that
cannot make a move loses the game.

They play x rounds of the game, where n may be
different for each round. Assuming Maria always
goes first and both players play optimally,
determine who the winner of each game is.
"""


def isWinner(x, nums):
    """
    a winner is found at the end
    """
    maria, ben, primes, maxFactor = 0, 0, 0, 0
    maxFactors = [3, 10, 31, 100]

    for i in range(x):
        max = nums[i]

        if max / 10 <= 1:
            maxFactor = maxFactors[0]
        elif max / 10 <= 10:
            maxFactor = maxFactors[1]
        elif max / 10 <= 100:
            maxFactor = maxFactors[2]
        elif max / 10 <= 1000:
            maxFactor = maxFactors[3]

        for n in range(2, max + 1):
            for f in range(2, maxFactor):
                if n % f is 0:
                    continue
                primes += 1
        if primes % 2 is 0:
            ben += 1
        else:
            maria += 1
        primes = 0
    if maria == ben:
        return None
    return "Maria" if maria > ben else "Ben"

# def is_prime(x, nums):
#     if nums > 1:
#         for x in range(2, int(num/2)+1):
#             if (nums % x) == 0:
#                 return False
#     return True
