def selectionSort(n, A):
    cnt = 0
    for i in range(n):
        minj = i
        for j in range(i, n):
            if A[minj][1] > A[j][1]:
                minj = j
        if i != minj:
            A[i], A[minj] = A[minj], A[i]
            cnt += 1
    return A


def bubbleSort(n, A):
    flag = True
    cnt = 0
    while flag:
        flag = False
        for j in range(n - 1, 0, -1):
            if A[j - 1][1] > A[j][1]:
                A[j - 1], A[j] = A[j], A[j - 1]
                cnt += 1
                flag = True
    return A


def stableSort(input, output):
    n = len(input)
    for i in range(n):
        for j in range(i + 1, n):
            for a in range(n):
                for b in range(a + 1, n):
                    if input[i][1] == input[j][1] and input[i] == output[b] and input[j] == output[a]:
                        return print("Not stable")
    return print("Stable")


if __name__ == '__main__':
    n = int(input())
    R = list(map(str, input().split()))
    C = R[:]
    D = R[:]  #????????¨?????????
    SR = selectionSort(n, R)
    BR = bubbleSort(n, C)
    print(*BR)
    stableSort(D,BR)
    print(*SR)
    stableSort(D,SR)