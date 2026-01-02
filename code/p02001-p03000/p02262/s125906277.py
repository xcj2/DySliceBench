import math

def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j>=0 and A[j]>v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v

def shellSort(A, n):
    global cnt
    cnt = 0
    g = []
    h = 1
    while h <= n:
        g.append(h)
        h = h * 3 + 1
    g.reverse()
    m = len(g)
    print(m)
    show(g)
    for i in range(0, m):
        insertionSort(A, n, g[i]) 

def show(A):
    L = list(map(str, A))
    print(" ".join(L))

n = int(input())
A = [int(input()) for i in range(n)]

shellSort(A, n)
print(cnt)
for i in A:
    print(i)
