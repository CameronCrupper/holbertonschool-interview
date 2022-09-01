#!/usr/bin/env python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """
    going thru lockboxxes and seeing if they can open the next if all true
    return true otherwise return false
    """
    keyset = {0}

    for key in boxes[0]:
        if (0 <= key < len(boxes)) and key not in keyset:
            boxes[0].extend(boxes[key])
            keyset.add(key)

    return len(keyset) == len(boxes)
