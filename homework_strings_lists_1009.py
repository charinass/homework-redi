arr = [0, 0, 1, 1, 1, 2, 3, 4, 4, 6, 6, 6, 8, 4, 4]
arrTmp = []
arrResult = []

for i in range(len(arr) - 1):
    arrTmp.append(arr[i])

    if not (arr[i] == arr[i+1]):
        arrResult.append(arrTmp)
        arrTmp = []

arrTmp.append(arr[len(arr)-1])
arrResult.append(arrTmp)  # last element

print(arrResult)
