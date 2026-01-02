
def BubbleSort(N, C):
    C = [] + C
    for i in range(N):
        for j in range(N-1, i, -1):
            if C[j][1] < C[j-1][1]:
                C[j], C[j-1] = C[j-1], C[j]
    return C

def SelectionSort(N, C):
    C = [] + C
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[minj][1] > C[j][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C

def CompareSuit(L1, L2):
    suit1, suit2 = "", ""
    for i in range(len(L1)):
        suit1 = suit1 + L1[i]
        suit2 = suit2 + L2[i]
    if suit1 == suit2:
        return "Stable"
    else:
        return "Not stable"

N = int(input())
C = input().split()

C1 = BubbleSort(N, C)
C2 = SelectionSort(N, C)

print(" ".join(C1))
print(CompareSuit(C1, C1))
print(" ".join(C2))
print(CompareSuit(C1, C2))