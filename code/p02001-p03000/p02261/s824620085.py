def readInt():
  return int(input())


def bubleSort(l, n):
    for i in range(1, n):
        for j in range(n - i):
            if l[j][1] > l[j + 1][1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def selectionSort(l, n):
    for i in range(n):
        mini = i
        for j in range(i, n):
            if l[j][1] < l[mini][1]:
                mini = j
        l[i], l[mini] = l[mini], l[i]
    return l

def readInts():
  return [int(i) for i in input().split()]
N = readInt()
AS = input().split()

import copy

stable = bubleSort(copy.deepcopy(AS), N)
notstable = selectionSort(AS, N)

print(*stable)
print('Stable')
print(*notstable)
if stable == notstable:
    print('Stable')
else:
    print('Not stable')

