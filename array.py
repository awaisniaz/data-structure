def findAndBuy(arr):
    min = arr[0]
    index = 0
    maxProfit = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            index = i
    for j in range(index+1,len(arr)):
        currentProfit = arr[j] - min
        if currentProfit > maxProfit:
            maxProfit = currentProfit
    return maxProfit




print(findAndBuy([7, 1, 5, 3, 6, 4]))