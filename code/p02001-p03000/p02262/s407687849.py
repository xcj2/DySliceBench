def printing(m, G, cnt, A):
    print(m)
    for i in range(len(G)):
        if i != len(G) - 1:
            print(G[i], end=' ')
        else:
            print(G[i])

    print(cnt)
    for i in A:
        print(i)

def insertionSort(A, n, g, cnt):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v
    return cnt


def shellSort(A, n, cnt):

    m = 0
    G = [1]
    while True:
        formulate = 3 * G[m] + 1
        if N > formulate:
            G.append(formulate)
        else:
            break
        m += 1

    for i in range(len(G) // 2):
        G[i], G[-1 - i] = G[-1 - i], G[i]

    for i in range(m + 1):
        cnt = insertionSort(A, n, G[i], cnt)

    printing(m + 1, G, cnt, A)


N = int(input())
inputList = []
for i in range(N):
    inputList.append(int(input()))

# inputList = list(map(int, '''5
# 5 1 4 3 2'''.split()))
# N = inputList.pop(0)

cnt = 0
shellSort(inputList, N, cnt)
