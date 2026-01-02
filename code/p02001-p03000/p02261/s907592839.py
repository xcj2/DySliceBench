import copy

class Card():
    def __init__(self, str):
        self.id = str
        self.sort = str[0]
        self.value = int(str[1])


def selectionSort(A, N):
    for i in range(N-1):
        minj = i
        for j in range(i, N):
            if A[j].value < A[minj].value:
                minj = j
        if i != minj:
            temp = A[i]
            A[i] = A[minj]
            A[minj] = temp

def bubbleSort(l, n):
    flag = 1
    while flag:
        flag = 0
        for i in range(n-1, 0, -1):
            if l[i].value < l[i-1].value:
                temp = l[i]
                l[i] = l[i-1]
                l[i-1] = temp
                flag = 1

def isStable(input, output, N):
    for i in range(N-1):
        for j in range(i+1, N):
            for a in range(N-1):
                for b in range(a+1, N):
                    if input[i].value == input[j].value and input[i] == output[b] and input[j] == output[a]:
                        return False
    return True

N = int(input())
A = list(map(Card, input().split()))
A_b = copy.copy(A)
A_s = copy.copy(A)

bubbleSort(A_b, N)
print(" ".join(map(lambda x: x.id, A_b)))
if isStable(A, A_b, N):
    print("Stable")
else:
    print("Not stable")

selectionSort(A_s, N)
print(" ".join(map(lambda x: x.id, A_s)))
if isStable(A, A_s, N):
    print("Stable")
else:
    print("Not stable")

