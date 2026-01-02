#shell sort
import math
count = 0


def printout(array, n):
    output = ""
    for i in range(n - 1):
        output += str(array[i]) + " "
    output += str(array[n - 1])
    print(output)


def insertionSort(A, n, g):
    global count
    for i in range(g,n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            count += 1
        A[j+g] = v


def shellSort(A, n):
    a = 1
    G = []
    while a <= n:
        G.append(a)
        a = 3*a + 1
    G.reverse()
    m = len(G)
    print(m)
    printout(G,m)
    for i in range(m):
        insertionSort(A, n, G[i])
    print(count)
    for i in range(n):
        print(A[i])


N = int(input())
array = []
for i in range(N):
    array.append(int(input()))
shellSort(array,N)
