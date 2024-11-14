import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    length_array = len(arr[0])
    diagonal_left = 0
    diagonal_right = 0
    left = 0
    right = length_array - 1
    for x in arr:
        diagonal_left += x[left]
        diagonal_right += x[right]
        left += 1
        right -= 1

    return abs(diagonal_left - diagonal_right)


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    # fptr.write(str(result) + "\n")

    # fptr.close()
