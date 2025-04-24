#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    valley = False
    amount_of_valleys = 0
    level = 0
    valley_list = []
    for step in path:
        if step == "U":
            level += 1
        elif step == "D":
            level -= 1
        if level < 0:
            valley = True
        elif level >= 0:
            valley = False
        valley_list.append(valley)
    merged = []
    for i, val in enumerate(valley_list):
        if i == 0 or val != valley_list[i - 1]:
            merged.append(val)

    for i in merged:
        if i == True:
            amount_of_valleys += 1
    return amount_of_valleys

if __name__ == "__main__":
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
