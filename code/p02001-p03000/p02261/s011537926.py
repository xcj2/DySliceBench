def BubbleSort(C, N):
    for i in range(N):
        for j in range(N - 1, i, -1):
            if int(C[j][1]) < int(C[j - 1][1]):
                C[j], C[j - 1] = C[j - 1], C[j]
    return C

def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if int(C[j][1]) < int(C[minj][1]):
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C

def isStable(B, S, N):
    for i in range(N):
        if B[i] != S[i]:
            return False
    return True

N = int(input())
B = input().split()
S = B[:]
B = BubbleSort(B, N)
S = SelectionSort(S, N)
mes = "Stable" if isStable(B, S, N) else "Not stable"
print(" ".join(B))
print("Stable")
print(" ".join(S))
print(mes)