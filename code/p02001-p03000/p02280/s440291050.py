import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1
        self.sibling = -1
        self.typ = "leaf"
        self.degree = 0

def getDepth(G, v, d=0):
    G[v].depth = d
    if G[v].right != -1:
        getDepth(G, G[v].right, d+1)
    if G[v].left != -1:
        getDepth(G, G[v].left, d+1)

def getHeight(G, v):
    h1, h2 = 0, 0
    if G[v].right != -1:
        getHeight(G, G[v].right)
        h1 = G[G[v].right].height + 1
    if G[v].left != -1:
        getHeight(G, G[v].left)
        h2 = G[G[v].left].height + 1
    G[v].height = max(h1, h2)

def main():
    n = int(input())
    G = [Node() for _ in range(n)]
    for _ in range(n):
        idx, l, r = map(int, input().split())
        G[idx].left = l
        G[idx].right = r
        if l != -1:
            G[l].parent = idx
            G[idx].typ = "internal node"
            G[idx].degree += 1
        if r != -1:
            G[r].parent = idx
            G[idx].typ = "internal node"
            G[idx].degree += 1
        if l != -1 and r != -1:
            G[l].sibling = r
            G[r].sibling = l
    root = [i for i, x in enumerate(G) if x.parent == -1][0]
    G[root].typ = 'root'
    getDepth(G, root)
    getHeight(G, root)
    for i, x in enumerate(G):
        print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(i, x.parent, x.sibling, x.degree, x.depth, x.height, x.typ))

if __name__ == '__main__': main()
