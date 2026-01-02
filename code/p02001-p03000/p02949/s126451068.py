import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
import queue

NINF = -1000000000

def reachable(n, vtxs):
    visited = [0 for i in range(n)]
    visited[0] = 1

    qu = queue.Queue()
    qu.put(0)
    while(not qu.empty()):
        curr = qu.get()
        for next in vtxs[curr]:
            if visited[next] == 0:
                visited[next] = 1
                qu.put(next)

    return visited

def reachable_rev(n, revs):
    visited = [0 for i in range(n)]
    visited[n-1] = 1
    qu = queue.Queue()
    qu.put(n - 1)
    while(not qu.empty()):
        curr = qu.get()
        for next in revs[curr]:
            if visited[next] == 0:
                visited[next] = 1
                qu.put(next)

    return visited



def bellman(n, m, edges, vtxs, revs):
    cost = [NINF for i in range(n)]
    cost[0] = 0
    tgts = [0]
    loop = 0
    final = False
    reach = reachable(n, vtxs)
    revreach = reachable_rev(n, revs)
    while(True):
        flag = False
        if loop > n:
            final = True
            break
        for e in edges:
            # print(e, cost)
            if cost[e[1]] < cost[e[0]] + e[2]:
                point = e[1]
                ppoint = e[0]
                # print("point", point)
                if reach[point] and revreach[point]:
                    if reach[ppoint] and revreach[ppoint]:
                        cost[e[1]] = cost[e[0]] + e[2]
                        flag = True
                        # print("update")
        if not flag:
            break
        loop += 1
        # print("loop", loop, cost)


    # print("judge", reach, revreach)
    if final:
        for e in edges:
            # print(e, cost)
            if cost[e[1]] < cost[e[0]] + e[2]:
                point = e[1]
                ppoint = e[0]
                # print("point", point)
                if reach[point] and revreach[point]:
                    if reach[ppoint] and revreach[ppoint]:
                        return -1

    if reach[-1] == 0:
        return -1

    return max(0, cost[-1])

n, m , p= getList()
vtxs = [[] for i in range(n)]
revs = [[] for i in range(n)]
edges = []

for i in range(m):
    a, b, c = getList()
    vtxs[a-1].append(b-1)
    revs[b-1].append(a-1)
    edges.append((a-1, b-1, c - p))

# print(edges)
print(bellman(n, m, edges, vtxs, revs))

