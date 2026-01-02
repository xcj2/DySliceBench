cnt = 0

def insertionsort(A,n,g):
    global cnt
    for i in range(g,n):
        v = A[i]
        j = i-g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v

def shellsort(A,n):
    h = 1
    G = []
    while h <= len(A):
        G.append(h)
        h = h*3+1
    G.reverse()
    m = len(G)
    for i in range(m):
        insertionsort(A,n,G[i])
    return m,G
def main():
    n = int(input())
    A = []
    for _ in range(n):
        A.append(int(input()))
    m,G = shellsort(A,n)
    ##print("-----------")
    print(m)
    print(*G)
    print(cnt)
    for i in A:
        print(i)

if __name__ == "__main__":
    main()
