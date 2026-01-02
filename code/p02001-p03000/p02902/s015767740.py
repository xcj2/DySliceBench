def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    #inf = 10**17
    #mod = 10**9 + 7

    n,m = map(int, input().split())
    adj = [[] for _ in range(n)] #頂点数, 場合によって変える
    for _ in range(m):
        a,b = map(int, input().split())
        adj[a-1].append(b-1)

    # 始点, 今回見る点
    def dfs(s, v):
        for nv in adj[v]:
            if nv == s:
                return [v]
            if visited[nv] == 1:
                continue
            visited[nv] = 1
            res = dfs(s, nv)
            if res != -1:
                res.append(v)
                return res
        return -1


    for s in range(n):
        visited = [0]*n
        visited[s] = 1
        heiro = dfs(s, s)
        if heiro != -1:
            break
    else:
        print(-1)
        exit()
    heiro = heiro[::-1]

    def graph(s, g):
        res = [s]
        d = deque([s])
        for i in range(len(heiro)):
            if heiro[i] == s:
                idx = i
                break
        while d:
            v = d.popleft()
            for nv in adj[v]:
                if visited[nv] == 1 and nv == g:
                    res.append(nv)
                    return res
            d.append(heiro[idx+1])
            res.append(heiro[idx+1])
            idx += 1
            if idx == len(heiro)-2:
                idx = -1
            #ここ
            if res[-1] == heiro[heiro.index(s)-1]:
                return res

    while True:
        heiro.append(heiro[0])
        visited = [0]*n
        f = 0
        for i in heiro:
            visited[i] = 1
        new_heiro = [heiro[0]]
        for i in range(len(heiro)-1):
            for nv in adj[heiro[i]]:
                if visited[nv] == 1 and nv != heiro[i+1]:
                    new_heiro = graph(nv, heiro[i])
                    f = 1
                    break
            else:
                new_heiro.append(heiro[len(new_heiro)])
            if f:
                heiro = new_heiro
                break
        else:
            break

    print(len(heiro)-1)
    for i in heiro[:-1]:
        print(i+1)

if __name__ == '__main__':
    main()