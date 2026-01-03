import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,M = LI()
    g = [i for i in range(0,N+M+1)]
    g_num = [0] + [1 for _ in range(N)] + [0 for _ in range(M)]
    def find(x):
        if g[x] == x: return x
        g[x] = find(g[x])
        return g[x]

    def union(x,y):
        if find(x) == find(y): return
        g_num[g[x]] += g_num[g[y]]
        g_num[g[y]] = 0
        g[g[y]] = g[x]


    for i in range(1,N+1):
        for l in LI()[1:]: union(i,N+l)

    if g_num[N] == N:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()