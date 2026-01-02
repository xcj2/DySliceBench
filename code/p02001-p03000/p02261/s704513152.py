def bubbleSort(A, N):
    cnt = 0
    flg = True
    while flg:
        flg = False
        for i in range(N - 1):
            if A[i][1] > A[i + 1][1]:
                tmp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = tmp
                flg = True
                cnt += 1
    return A, cnt


def selectionSort(A, N):
    cnt = 0
    for i in range(N):
        minJ = i
        for j in range(i, N):
            if A[minJ][1] > A[j][1]:
                minJ = j
        if A[i][1] != A[minJ][1]:
            tmp = A[i]
            A[i] = A[minJ]
            A[minJ] = tmp
            cnt += 1
    return A, cnt


def resolve():
    import copy
    N = int(input())
    A = [i for i in input().split()]
    B = copy.deepcopy(A)
    ansA, cnt = bubbleSort(A, N)
    print(*ansA)
    print("Stable")
    ansB, cnt = selectionSort(B, N)
    print(*ansB)
    if ansA == ansB:
        print("Stable")
    else:
        print("Not stable")


resolve()

