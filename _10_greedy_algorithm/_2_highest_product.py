"""
Given an array of N integers.
Find the highest product by multiplying 3 elements.

"""

def highestProduct(array):
    a = sorted(array)

    highest_3 = a[-1]*a[-2]*a[-3]
    lowest_2_highest_1 = a[0]*a[1]*a[2]

    return max(highest_3, lowest_2_highest_1)