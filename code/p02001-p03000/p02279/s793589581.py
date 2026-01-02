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
    for _ in range(n):
        ikc = LI()
        id = ikc[0]
        # k = ikc[1]
        c = ikc[2:]
        children[id] = c

    parent = [-1]*n
    for i, e in enumerate(children):
        for j in e:
            parent[j] = i

    depth = [-1]*n
    root = parent.index(-1)
    depth[root] = 0
    que = collections.deque()
    que.append(root)
    while que:
        c = que.popleft()
        for i in children[c]:
            if depth[i]==-1:
                que.append(i)
                depth[i] = depth[c] + 1

    node_type = ['']*n
    for i in range(n):
        if parent[i]==-1:
            node_type[i] = 'root'
        elif not children[i]:
            node_type[i] = 'leaf'
        else:
            node_type[i] = 'internal node'

    for i in range(n):
        print('node {0}: parent = {1}, depth = {2}, {3}, {4}'.format(i, parent[i], depth[i], node_type[i], children[i]))

if __name__ == '__main__':
    resolve()

