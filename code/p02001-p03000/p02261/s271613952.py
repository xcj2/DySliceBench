def bubbleSort(C, N):
    for i in range(0, N):
        for j in range(i+1, N):
            if int(C[N-j+i][1]) < int(C[N-j+i-1][1]):
                (C[N-j+i], C[N-j+i-1]) = (C[N-j+i-1], C[N-j+i])
    print(" ".join(C))

def selectionSort(C, N):
    count = 0
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if int(C[j][1])<int(C[minj][1]):
                minj = j
        if minj != i:
            (C[i], C[minj]) = (C[minj], C[i])
            count += 1
    print(" ".join(C))

def isStable(C1, C2, N):
    for i in range(N):
        if C1[i] != C2[i]:
            return "Not stable"
    return "Stable"

n = int(input())
card = list(input().split())
card2 = card[:]

bubbleSort(card, n)
print("Stable")
selectionSort(card2, n)
print(isStable(card, card2, n))





