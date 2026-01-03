import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N = NI()
    xy = [LI() for _ in range(N)]

    x = [(xy[i][0],i) for i in range(N)]
    y = [(xy[i][1],i) for i in range(N)]

    x.sort()
    y.sort()

    edge = []
    p,i = x[0]
    for q,j in x[1:]:
        edge.append((q-p,i,j))
        p,i = q,j

    p,i = y[0]
    for q,j in y[1:]:
        edge.append((q-p,i,j))
        p,i = q,j

    edge.sort()

    g = [i for i in range(N + 1)]
    g_num = [1 for i in range(N + 1)]

    def find(x):
        if g[x] == x: return x
        g[x] = find(g[x])
        return g[x]

    def union(x, y):
        if find(x) == find(y): return
        if g_num[g[x]] < g_num[g[y]]: x, y = y, x
        g_num[g[x]] += g_num[g[y]]
        g_num[g[y]] = 0
        g[g[y]] = g[x]

    ans = 0
    for v,i,j in edge:
        if find(i) != find(j):
            ans += v
            union(i,j)

    print(ans)



if __name__ == '__main__':
    main()