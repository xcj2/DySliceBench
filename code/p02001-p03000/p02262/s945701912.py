def insertionSort(A, N, g):
    global cnt
    for i in range(g, N):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v


def shellSort(A, n):
    global cnt
    G = []
    m = 1
    G.append(1)
    while 3*G[-1]+1 <= n:
        g = G[-1]
        G.append(g*3+1)
        m += 1
    G = sorted(G, reverse=True)
    for i in range(m):
        g = G[i]
        insertionSort(A, n, G[i])

    print(m)
    print(*G)
    print(cnt)
    for a in A:
        print(a)


def main():
    global cnt
    cnt = 0
    N = int(input())
    A = [int(input()) for i in range(N)]
    shellSort(A, N)

 
if __name__ == '__main__':
    main()

