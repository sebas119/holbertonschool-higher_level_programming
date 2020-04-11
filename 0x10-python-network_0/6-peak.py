#!/usr/bin/python3
# Find a peak function


def find_peak(list_nums):
    """Find a peak element and return it"""

    size = len(list_nums)

    if size == 0:
        return None
    elif size == 1:
        return list_nums[0]
    elif size == 2:
        return max(list_nums)

    left = 0
    right = size - 1

    while (left < right):
        m = int((left + right + 1) / 2)

        if list_nums[m - 1] > list_nums[m]:
            right = m - 1
        else:
            left = m
    # Left == Right
    return list_nums[left]
