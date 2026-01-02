import copy

N = int(input())
C = list(list(input().split()))
Cb, Cs = copy.copy(C), copy.copy(C)


def BubbleSort(C, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if C[j-1][1] > C[j][1]:
                C[j-1], C[j] = C[j], C[j-1]
    for i in range(N):
        C[i] = "".join(C[i])
    print(" ".join(map(str, C)))


def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i,N):
            if C[minj][1] > C[j][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
    for i in range(N):
        C[i] = "".join(C[i])
    print(" ".join(map(str, C)))

def StableCheck(Cin, Cout, N):
    for i in range(1,10):
        check1, check2 = [], []
        for j1 in Cin:
            if str(i) in j1:
                check1.append(j1)
        for j2 in Cout:
            if str(i) in j2:
                check2.append(j2)
        if check1 != check2:
            print("Not stable")
            exit()
    print("Stable")

BubbleSort(Cb, N)
StableCheck(C, Cb, N)
SelectionSort(Cs, N)
StableCheck(C, Cs, N)
