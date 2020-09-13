arr = [0, 0, 1, 1, 1, 2, 3, 4, 4, 6, 6, 6, 8, 4, 4]
arrTmp = []
arrLen = len(arr)
arrResult = []

for i in range(arrLen - 1):
    arrTmp.append(arr[i])

    if not (arr[i] == arr[i+1]):
        arrResult.append(arrTmp)
        arrTmp = []

arrTmp.append(arr[arrLen-1])
arrResult.append(arrTmp)

print(arrResult)
