from collections import deque

N = int(input())
Sss = [input() for _ in range(N)]

adjL = [[] for _ in range(N)]
for i, Ss in enumerate(Sss):
    for j, S in enumerate(Ss):
        if S == '1':
            adjL[i].append(j)

def IsBipartiteGraph(adjList):
    def bfs(vSt):
        colors[vSt] = 1
        Q = deque([vSt])
        while Q:
            vNow = Q.popleft()
            color = colors[vNow]
            for v2 in adjList[vNow]:
                if colors[v2] == color:
                    return False
                elif colors[v2] == 0:
                    colors[v2] = -color
                    Q.append(v2)
        return True
    numV = len(adjList)
    colors = [0] * numV
    for vSt in range(numV):
        if colors[vSt] != 0: continue
        if not bfs(vSt):
            return False
    return True

def WarshallFloyd(adjList):
    numV = len(adjList)
    D = [[float('inf')]*numV for _ in range(numV)]
    for u, adj in enumerate(adjList):
        for v in adj:
            D[u][v] = 1
        D[u][u] = 0
    for k in range(numV):
        Dk = D[k]
        for i in range(numV):
            Di = D[i]
            Dik = Di[k]
            for j in range(numV):
                D2 = Dik + Dk[j]
                if D2 < Di[j]:
                    D[i][j] = D2
    return D


if not IsBipartiteGraph(adjL):
    print(-1)
else:
    distss = WarshallFloyd(adjL)
    maxDist = max(map(max, distss))
    print(maxDist+1)
