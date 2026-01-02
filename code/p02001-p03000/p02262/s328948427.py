n = int(input())
A = [int(input()) for i in range(n)]

def getG(n):
    gn = 1
    G = [1]
    while 3*gn + 1 < n:
        gn = G[-1]*3 + 1
        G.append(gn)
    return G[::-1]

def insertionSort(A, n, g, cnt):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
            A[j+g] = v
    return A, cnt

def shellSort(A, n):
    G = getG(n)
    m = len(G)
    cnt = 0
    for i in range(m):
        A, cnt_l = insertionSort(A, n, G[i], cnt)
        cnt = cnt_l
    return A, m, G, cnt

A, m, G, cnt = shellSort(A, n)
print(m)
print(" ".join([str(s) for s in G]))
print(cnt)
for a in A:
    print(a)
