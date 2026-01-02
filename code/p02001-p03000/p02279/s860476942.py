import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.parent = -1
        self.typ = "leaf"

def dfs(G, v, d=0):
    G[v].depth = d
    for child in G[v].childlen:
        dfs(G, child, d+1)

def main():
    N = int(input())
    G = [Node() for _ in range(N)]
    for _ in range(N):
        idx, k, *childlen = map(int, input().split())
        G[idx].childlen = childlen
        if k:
            G[idx].typ = "internal node"
        for child in childlen:
            G[child].parent = idx
    root = [i for i, x in enumerate(G) if x.parent == -1][0]
    G[root].typ = 'root'
    dfs(G, root)
    for i, x in enumerate(G):
        print('node {}: parent = {}, depth = {}, {}, [{}]'.format(i, x.parent, x.depth, x.typ, ', '.join(list(map(str, x.childlen)))))

if __name__ == '__main__': main()
