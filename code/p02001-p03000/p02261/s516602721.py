def bubbleSort(A, N):
    flag = 1
    while flag:
        flag = 0
        for j in range(N-1, 0, -1):
            if A[j][1] < A[j-1][1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = 1
    print(*A)
    return A


def selectionSort(A, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j][1] < A[minj][1]:
                minj = j
        A[i], A[minj] = A[minj], A[i]

    print(*A)
    return A


def isStable(input, output, N):
    for i in range(N):
        for j in range(i + 1, N):
            for a in range(N):
                for b in range(a + 1, N):
                    if input[i][1] == input[j][1] and input[i] == output[b] and input[j] == output[a]:
                        print("Not stable")
                        return False
    print("Stable")
    return True

arr_length = int(input())
arr_num = [i for i in input().split(" ")]

isStable(arr_num, bubbleSort(list(arr_num), arr_length), arr_length)

isStable(arr_num, selectionSort(list(arr_num), arr_length), arr_length)
