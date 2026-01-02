def insertion_sort(A, n, g, cnt):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and v < A[j]:
            A[j+g] = A[j]
            j -= g
            cnt += 1
            A[j+g] = v
    return cnt

def shell_sort(A, n):
    cnt = 0
    h = 1
    g = []
    while h <= n:
        g.append(h)
        h = 3*h + 1
    g.reverse()
    m = len(g)
    for i in range(m):
        cnt = insertion_sort(A, n, g[i], cnt)
    show(n, m, g, A, cnt)

def show(n, m, G, A, cnt):
    print(m)
    for i in range(m):
        if i != m-1:
            print(G[i], end = " ")
        else:
            print(G[i])
    print(cnt)
    for i in range(n):
        print(A[i])

if "__main__" == __name__:
    n = int(input())
    data = []
    for i in range(n):
        data.append(int(input()))
    shell_sort(data, n)
