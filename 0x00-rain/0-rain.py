#!/usr/bin/python3

def rain(walls):

    L = len(walls)
    water = 0

    for i in range(1, L - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]

        for j in range(i + 1, L):
            right = max(right, walls[j])

        water = water + (min(left, right) - walls[i])
    return water
