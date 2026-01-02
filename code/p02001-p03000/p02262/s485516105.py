import math

N = int(input())
A = list(int(input()) for _ in range(N))

def insertionSort(A,n,g,cnt):
    for i in range(g,n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v
    return cnt

def shellSort(A,n):
    cnt = 0
    G = []
    bet = 0
    while True:
        bet = 3*bet + 1
        if bet <= n:
            G.insert(0,bet)
        else:
            break
    m = len(G)

    for i in range(m):
        cnt = insertionSort(A,n,G[i],cnt)
    print(m)
    outputNumList(G)
    print(cnt)

def outputNumList(A):
    tmp = map(str,A)
    text = " ".join(tmp)
    print(text)

shellSort(A,N)
for k in range(N):
    print(A[k])
