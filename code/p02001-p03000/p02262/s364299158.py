def insertionSort(A, g, count):
    N = len(A)
    for i in range(g, N):
        j = i - g
        temp = A[i]
        while j >= 0 and A[j] > temp:
            A[j + g] = A[j]
            j -= g
            count += 1
        A[j + g] = temp
    return A, count


def shellSort(A):
    n = len(A)
    count = 0
    h = 1
    G = []
    while (True):
        if h > n:
            break
        G.append(h)
        h = 3 * h + 1
    m = len(G)
    G.reverse()
    for i in range(m):
        A, count = insertionSort(A, G[i], count)
    return m, G, count, A


def listFromInput():
    N = int(input())
    numbers = []
    for i in range(N):
        numbers.append(int(input()))
    return numbers


A = listFromInput()
m, G, count, A = shellSort(A)
print(m)
print(" ".join(list(map(str, G))))
print(count)
for i in A:
    print(i)