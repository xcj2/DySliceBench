import copy

def BubbleSort(C, N):
    stable = True

    for i in range(N):
        for j in range(i + 1, N)[::-1]:
            if C[j][2] < C[j - 1][2]:
                C[j], C[j - 1] = C[j - 1], C[j]

    
    AnswerPrint(C, IsStable(C))


def SelectionSort(C, N):
    stable = True

    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j][2] < C[minj][2]:
                minj = j

        C[i], C[minj] = C[minj], C[i]

    AnswerPrint(C, IsStable(C))


def IsStable(C):
    for index, c in enumerate(C):
        for i in range(index, len(C)):
            if (c[2] == C[i][2]) and (c[0] > C[i][0]):
                return False

    return True
                

def AnswerPrint(C, stable):
    out = ["{}{}".format(c[1], c[2]) for c in C]
    print(" ".join(out))

    if stable:
        print("Stable")
    else:
        print("Not stable")



N = int(input())
inp = input().split()
C = [[index, c[0], int(c[1])] for index, c in enumerate(inp)]

BubbleSort(copy.copy(C), N)
SelectionSort(copy.copy(C), N)
