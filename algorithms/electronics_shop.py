#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    total_expense = []
    max_price = -1
    for keyboard in keyboards:
        for drive in drives:
            total_expense.append(keyboard + drive)

    for price in total_expense:
        if price <= b and price >= max_price:
            max_price = price
    return max_price



if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

