def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

from collections import deque

n = getN()
paths = [[] for i in range(n)]
for i in range(n-1):
    a,b,c = getList()
    paths[a-1].append((b-1,c))
    paths[b-1].append((a-1,c))

def findroot(tree):
    for i, v in enumerate(tree):
        if len(v) == 1:
            return i

root = findroot(paths)


def getdist(tree, root):
    d = deque([root])
    dist = [-1 for i in range(len(tree))]
    dist[root] = 0
    while(d):
        #print(d, dist)
        nxt = d.pop()
        tmp = dist[nxt]
        for edge in tree[nxt]:
            v, c = edge
            if dist[v] == -1:
                d.append(v)
                dist[v] = tmp + c

    return dist

distlist = getdist(paths, root)
for i in distlist:
    print(i % 2)