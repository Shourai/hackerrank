def birthdayCakeCandles(candles):
    max = 0
    amount = 0
    for i in candles:
        if i > max:
            max = i
            amount = 1
        elif i == max:
            amount += 1
        else:
            continue

    return amount

birthdayCakeCandles([3,2,1,3])
