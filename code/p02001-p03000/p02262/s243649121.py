cnt = 0

def insertionSort(A, n, g):
    global cnt
    for i in range(g,n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v

def shellSort(A, n):
    h = 1
    G = []
    while h <= n:
        G.append(h)
        h = 3*h + 1

    for g in reversed(G):
        insertionSort(A, n, g)

    return G

def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))

    G = shellSort(A, N)
    
    # output
    print(len(G))
    for g in reversed(G):
        if g == G[0]:
            print(g)
        else:
            print(g, end=" ")
    print(cnt)
    for a in A:
        print(a)

if __name__ == "__main__":
    main()
