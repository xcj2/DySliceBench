import sys
readline = sys.stdin.readline

import collections
class Dinic:
    def __init__(self, vnum):
        self.edge = [[] for i in range(vnum)]
        self.n = vnum
        # infはint型の方が良いかもね
        self.inf = float('inf')
    def addedge(self, st, en, c):
        self.edge[st].append([en, c, len(self.edge[en])])
        self.edge[en].append([st, 0, len(self.edge[st])-1])
    def bfs(self, vst):
        dist = [-1]*self.n
        dist[vst] = 0
        Q = collections.deque([vst])
        while Q:
            nv = Q.popleft()
            for vt, c, r in self.edge[nv]:
                if dist[vt] == -1 and c > 0:
                    dist[vt] = dist[nv] + 1
                    Q.append(vt)
        self.dist = dist
    def dfs(self, nv, en, nf):
        nextv = self.nextv
        if nv == en:
            return nf
        dist = self.dist
        ist = nextv[nv]
        for i, (vt, c, r) in enumerate(self.edge[nv][ist:], ist):
            if dist[nv] < dist[vt] and c > 0:
                df = self.dfs(vt, en, min(nf, c))
                if df > 0:
                    self.edge[nv][i][1] -= df
                    self.edge[vt][r][1] += df
                    return df
            nextv[nv] += 1
        return 0
    def getmf(self, st, en):
        mf = 0
        while True:
            self.bfs(st)
            if self.dist[en] == -1:
                break
            self.nextv = [0]*self.n
            while True:
                fl = self.dfs(st, en, self.inf)
                if fl > 0:
                    mf += fl
                else:
                    break
        return mf



N, M = map(int, readline().split())
A = [list(map(int, readline().split())) for _ in range(N)]


B = [[None]*M for _ in range(N)]

st = 2*N
en = 2*N+1
used = set()
for num in range(M):
    T = Dinic(2*N+2)
    for i in range(N):
        T.addedge(st, i, 1)
        T.addedge(N+i, en, 1)
        for j in range(M):
            aij = A[i][j]
            if aij not in used:
                T.addedge(i, N+(aij-1)//M, 1)
    
    T.getmf(st, en)
    for i in range(N):
        candi = [e for e, cost, _ in T.edge[i+N] if cost == 1][0]
        for j in range(M):
            if A[candi][j] not in used and (A[candi][j]-1)//M == i:
                used.add(A[candi][j])
                B[candi][num] = A[candi][j]
                break
C = list(map(list, zip(*B)))
C = [sorted(c) for c in C]
C = list(map(list, zip(*C)))

for b in B:
    print(*b)

for c in C:
    print(*c)
