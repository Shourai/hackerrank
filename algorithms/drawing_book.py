#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import batched

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def pageCount(n, p):
    # Create array/list of pages
    if n % 2 == 0:
        pages = range(0, n + 2)
    else:
        pages = range(0, n + 1)
    book = list(batched(pages, 2))

    result = []

    # loop from left
    left_count = 0
    for page in book:
        if p in page:
            result.append(left_count)
        else:
            left_count += 1

    # look from right
    right_count = 0
    for i in range(len(book) - 1, 0, -1):
        if p in book[i]:
            result.append(right_count)
        else:
            right_count += 1

    return min(result)


if __name__ == "__main__":
    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)
    print(result)
