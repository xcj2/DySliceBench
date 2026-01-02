class Card:
    def __init__(self):
        self.suit = ""
        self.value = ""

def bubbleSort(C, N):
    flag = 1
    while flag:
        flag = False
        for j in reversed(range(1,N)):
            if C[j][1] < C[j-1][1]:
                C[j],C[j-1] = C[j-1],C[j]
                flag = True

def selectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i,N):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i],C[minj] = C[minj],C[i]

def check(L1,L2):
    if L1 == L2:
        return 'Stable'
    else:
        return 'Not stable'

N = int(input())
C = list(input().split())
from copy import deepcopy
L1 = deepcopy(C)
L2 = deepcopy(C)

bubbleSort(L1,N)
selectionSort(L2,N)

print(*L1)
print('Stable')
print(*L2)
print(check(L1,L2))
