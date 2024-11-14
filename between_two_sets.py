#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    divisorsA = []
    divisorsB = []

    for num in a:
        newSet = set()
        for i in range(num, max(b) + 1, num):
            newSet.add(i)
        divisorsA.append(newSet)

    for num in b:
        newSet = set()
        newSet.add(num)
        for i in range(1, num):
            if num % i == 0:
                newSet.add(i)
        divisorsB.append(newSet)

    # print(divisorsA.intersection(divisorsB))
    A = set.intersection(*divisorsA)
    B = set.intersection(*divisorsB)
    return len(set.intersection(A, B))


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    # fptr.write(str(total) + '\n')

    # fptr.close()
