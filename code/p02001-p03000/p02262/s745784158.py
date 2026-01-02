def insertionSort(A, N, g=1):
    global count
    for i in range(g, N):
        v = A[i]
        j = i-g
        while A[j] > v and j >= 0:
            A[j+g], A[j] = A[j], A[j+g]
            count += 1
            j -= g


def bubbleSort(A, N):
    flag = 1
    while flag:
        flag = 0
        for j in range(N-1, 0, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = 1


def selectionSort(A, N):
    for i in range(N):
        minidx = i
        for j in range(i, N):
            if A[j] < A[minidx]:
                minidx = j
        A[i], A[minidx] = A[minidx], A[i]


def shellSort_d(N):
    G = [1]
    i = 0
    while True:
        tmp = G[i] * 3 + 1
        if tmp < N:
            G.append(tmp)
            i += 1
        else:
            break
    G.reverse()
    return G


def shellSort(A, N):
    global count, G
    count = 0
    G = shellSort_d(N)
    for g in G:
        insertionSort(A, N, g)


N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

shellSort(A, N)

print(len(G))
print(" ".join(map(str,G)))
print(count)
for a in A:
    print(a)
