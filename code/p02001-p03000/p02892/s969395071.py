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

def getDiameterOfUnweightedGraph(adjList):
    numV = len(adjList)
    def bfs(vSt):
        costs = [-1] * numV
        costs[vSt] = cost = 0
        vs = [vSt]
        while vs:
            cost += 1
            v2s = []
            for v in vs:
                for v2 in adjList[v]:
                    if costs[v2] == -1:
                        costs[v2] = cost
                        v2s.append(v2)
            vs = v2s
        return cost - 1
    return max([bfs(vSt) for vSt in range(numV)])


if not IsBipartiteGraph(adjL):
    print(-1)
else:
    maxDist = getDiameterOfUnweightedGraph(adjL)
    print(maxDist+1)
