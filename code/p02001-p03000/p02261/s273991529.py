import copy

def printData(data) :
    for i, value in enumerate(data) :
        if i > 0 :
            print(" ", end = "")
        print(value[0] + str(value[1]), end = "")
    print()
    
def isStable(data1, data2) :
    for v1, v2 in zip(data1, data2) :
        if v1[0] != v2[0] :
            return "Not stable"
    return "Stable"

def bubbleSort(data, N) :
    flag = 1
    for i in range(N) :
        if not flag :
            break
        flag = 0
        for j in reversed(range(i + 1, N)) :
            if data[j][1] < data[j - 1][1] :
                buf = data[j]
                data[j] = data[j - 1]
                data[j - 1] = buf
                flag = 1
    printData(data)
    print("Stable")
    
def selectionSort(data, N) :
    for i in range(N) :
        minIdx = i
        for j in range(i + 1, N) :
            if data[j][1] < data[minIdx][1] :
                minIdx = j
        if minIdx != i :
            buf = data[minIdx]
            data[minIdx] = data[i]
            data[i] = buf
    printData(data)


N = int(input())
data = [list(value) for value in input().split()]
for value in data :
    value[1] = int(value[1])
    
copy_data1 = copy.deepcopy(data)
bubbleSort(copy_data1, N)
copy_data2 = copy.deepcopy(data)
selectionSort(copy_data2, N)
print(isStable(copy_data1, copy_data2))


