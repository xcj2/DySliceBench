import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    n = I()
    children = [[] for _ in range(n)]
    parent = [-1]*n
    sibling = [-1]*n
    for _ in range(n):
        ilr = LI()
        id = ilr[0]
        left = ilr[1]
        right = ilr[2]
        children[id] = (left, right)
        if left>=0:
            parent[left] = id
            sibling[left] = right
        if right>=0:
            parent[right] = id
            sibling[right] = left

    depth = [-1]*n
    root = parent.index(-1)
    depth[root] = 0
    que = collections.deque()
    que.append(root)
    while que:
        c = que.popleft()
        for i in children[c]:
            if i!=-1 and depth[i]==-1:
                que.append(i)
                depth[i] = depth[c] + 1

    height = [-1]*n
    def dfs(v):
        children_v = children[v]
        if children_v.count(-1)==2:
            height[v] = 0
        else:
            for i in children_v:
                if i!=-1:
                    height[v] = max(1 + dfs(i), height[v])
        return height[v]
    dfs(root)

    node_type = ['']*n
    for i in range(n):
        if parent[i]==-1:
            node_type[i] = 'root'
        elif children[i].count(-1)==2:
            node_type[i] = 'leaf'
        else:
            node_type[i] = 'internal node'

    for i in range(n):
        print('node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}'.format(i, parent[i], sibling[i], len(children[i])-children[i].count(-1), depth[i], height[i], node_type[i]))

if __name__ == '__main__':
    resolve()

