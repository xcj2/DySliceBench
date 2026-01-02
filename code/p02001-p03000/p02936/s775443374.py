import sys
sys.setrecursionlimit(200000)
from collections import deque


def read():
    N, Q = list(map(int, input().strip().split()))
    G = [list() for i in range(N+1)]
    PX = list()
    for i in range(N-1):
        a, b = list(map(int, input().strip().split()))
        G[a].append(b)
        G[b].append(a)
    for i in range(Q):
        px = list(map(int, input().strip().split()))
        PX.append(px)
    return N, Q, G, PX


def bfs(parent, G, C, V):
    q = deque()
    q.append(1)
    while len(q) > 0:
        parent = q.pop()
        V[parent] = True
        for child in G[parent]:
            if not V[child]:
                C[child] += C[parent]
                q.append(child)
    

def solve(N, Q, G, PX):
    C = [0 for i in range(N+1)]
    V = [False for i in range(N+1)]
    for p, x in PX:
        C[p] += x
    bfs(1, G, C, V)
    return ' '.join(map(str, C[1:]))
    

if __name__ == '__main__':
    inputs = read()
    print("{}".format(solve(*inputs)))
