def plusMinus(arr):
    length_array = len(arr)
    positive = 0
    negative = 0
    zero = 0

    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1

    print(positive / length_array)
    print(negative / length_array)
    print(zero / length_array)

