def miniMaxSum(arr):
    smallestList = arr.copy()
    smallestList.remove(max(smallestList))

    largestList = arr.copy()
    largestList.remove(min(largestList))

    print(f"{sum(smallestList)} {sum(largestList)}")

miniMaxSum([1, 3, 5, 7, 9])
