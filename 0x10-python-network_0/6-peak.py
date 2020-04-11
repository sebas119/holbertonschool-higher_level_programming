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

    for i in range(size):
        if ((i == 0 or list_nums[i] >= list_nums[i - 1]) and (i == size - 1 or list_nums[i] >= list_nums[i + 1])):
            return list_nums[i]
