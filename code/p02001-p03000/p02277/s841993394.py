n = int(input())
cL = []
for i in range(n):
    inputS = input()
    inputL = inputS.split()
    cL.append([inputS, int(inputL[1])])

def partition(A, l, r):
    pivot = A[r][1]
    minVI = l-1
    i = l
    while i < r:
        if A[i][1] <= pivot:
            minVI+=1
            A[i], A[minVI] = A[minVI], A[i]
        i+=1
    A[minVI+1], A[i] = A[i], A[minVI+1]
    return minVI+1

def quickSort(A, l, r):
    if l < r:
        pivotI = partition(A, l, r)
        quickSort(A, l, pivotI-1)
        quickSort(A, pivotI+1, r)

def merge(l, r):
    lI = 0
    rI = 0
    newL = []
    while lI < len(l) and rI < len(r):
        if l[lI][1] <= r[rI][1]:
            newL.append(l[lI])
            lI+=1
        else:
            newL.append(r[rI])
            rI+=1
    while lI < len(l):
        newL.append(l[lI])
        lI+=1
    while rI < len(r):
        newL.append(r[rI])
        rI+=1
    return newL

def mergeSort(curL):
    if len(curL) <= 1:
        return curL
    else:
        mid = len(curL)//2
        left = mergeSort(curL[:mid])
        right = mergeSort(curL[mid:])
        return merge(left, right)

mergeSorted = mergeSort(cL)
quickSort(cL, 0, len(cL)-1)
quickSorted = cL
if mergeSorted == quickSorted:
    print('Stable')
else:
    print('Not stable')
for v in quickSorted:
    print(v[0])

