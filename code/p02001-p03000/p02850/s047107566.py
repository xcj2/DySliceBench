import collections
import sys
sys.setrecursionlimit(10 ** 8)

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

class edge:
    def __init__(self, to, id): self.to, self.id = to, id

def main():
    N = Z()
    col = [0] * (N-1)
    G = collections.defaultdict(list)
    for i in range(N-1):
        a, b = ZZ()
        G[a].append(edge(b, i))
        G[b].append(edge(a, i))
    numCol = 0
    for i in range(1, N+1): numCol = max(numCol, len(G[i]))

    def dfs(v):
        colSet = set()
        for ed in G[v]:
            if col[ed.id] != 0: colSet.add(col[ed.id])
        c = 1
        for ed in G[v]:
            if col[ed.id] != 0: continue
            while c in colSet: c += 1
            col[ed.id] = c
            c += 1
            dfs(ed.to)

    dfs(1)
    print(numCol)
    for i in range(N-1): print(col[i])

    return

if __name__ == '__main__':
    main()
