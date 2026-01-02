import copy


def SelectionSort(arr, n):
    for i in range(n):
        mini = i
        for j in range(i, n):
            if arr[j]['val'] < arr[mini]['val']:
                mini = j
        if mini != i:
            arr[i], arr[mini] = arr[mini], arr[i]
    return


def BubleSort(arr, n):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j]['val'] < arr[j-1]['val']:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return


def isStable(inarr, comparr, n):
    i = 0
    while i < n:
        tmpVal = comparr[i]['val']
        for j in range(n):
            if inarr[j]['val'] == tmpVal:
                if inarr[j]['crd'] == comparr[i]['crd']:
                    if i != n - 1 and comparr[i+1]['val'] == tmpVal:
                        i += 1
                    else:
                        break
                else:
                    return 'Not stable'
        i += 1
    return 'Stable'


n = int(input())
arr = input().split()
tar = []

for s in arr:
    tar.append({'crd': s[0], 'val': s[1], 'str': s})

bub = copy.copy(tar)
BubleSort(bub, n)

prt = []
for s in bub:
    prt.append(s['str'])
print(*prt)
print(isStable(tar, bub, n))

bub = copy.copy(tar)
SelectionSort(bub, n)

prt = []
for s in bub:
    prt.append(s['str'])
print(*prt)
print(isStable(tar, bub, n))

