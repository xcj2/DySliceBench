cnt = 0
def InsertionSort(A, n, g):
    global cnt
    outA = A.copy()
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and outA[j] > v:
            outA[j + g] = outA[j]
            j -= g
            cnt += 1
        outA[j + g] = v
    return outA

def ShellSort(A, n):
    global cnt
    outA = A.copy()
    G = []
    h = n - 1
    while h >= 2:
        G.append(h)
        h = int((h - 1)//3)
    G.append(1)
    m = len(G)
    for i in range(0, m):
        outA = InsertionSort(outA, n, G[i])
    return outA, m, G, cnt
def printlist(L):
    for t in L[:-1]:
        print(t, end = ' ')
    print(L[-1])

n = int(input())
A = [0 for i in range(n)]
for i in range(n):
    A[i] = int(input())

A, m, G, cnt = ShellSort(A, n)
print(m)
printlist(G)
print(cnt)
for itm in A:
    print(itm)

