def showList(A, N):
    for i in range(N-1):
        print(A[i],end=' ')
    print(A[N-1])

def inserationSort(A, n, g, cnt):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v
    return A, cnt

def shellSort(A,n):
    cnt = 0
    G = [1]
    i = 0
    while G[i] < n:
        G.append(3*G[i]+1)
        i += 1
    G.pop(len(G)-1)
    G.reverse()
    for j in range(len(G)):
        A, cnt = inserationSort(A, n, G[j], cnt)
    return A, cnt, G

n = int(input())
A = []
cnt = 0
for i in range(n):
    A.append(int(input()))
A, cnt, G = shellSort(A,n)

if len(G) != 0:
    print(len(G))
    showList(G, len(G))
elif len(G) == 0:
    print(1)
    print(1)
if n != 1:
    print(cnt)
    for i in range(n):
        print(A[i])
elif n == 1:
    print(cnt)
    print(A[0])
