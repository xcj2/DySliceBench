def BubbleSort(C, N):

    for i in range(N):
        for j in range(N-1, i, -1):
            if C[j][1] < C[j-1][1]:
                C[j], C[j-1] = C[j-1], C[j]
    return C

def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C

def isStable(C1, C2, N):
    if C1 != C2:
        return "Not stable"
    return "Stable"

Num = int(input())
Cards = [x for x in input().split()]
card1 = BubbleSort(list(Cards), Num)
card2 = SelectionSort(list(Cards), Num)

print(" ".join(card1))
print(isStable(card1, card1, Num))
print(" ".join(card2))
print(isStable(card1, card2, Num))

