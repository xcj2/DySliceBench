import sys
input = sys.stdin.readline

def same_tree(node_a, node_b):
    if node_a.root() == node_b.root():
        return True

def unite(node_a, node_b):
    root_a = node_a.root()
    root_b = node_b.root()
    if root_a == root_b:
        return
    if root_b.depth > root_a.depth:
        root_a, root_b = root_b, root_a
    root_b.is_root = False
    root_b.parent = root_a
    root_a.depth = max(root_a.depth, root_b.depth+1)

class Node:
    def __init__(self):
        self.is_root = True
        self.parent = None
        self.depth = 1
    
    def root(self):
        node = self
        while not node.is_root:
            node = node.parent
        return node

def main():
    N, M = map(int, input().split())
    kl = [list(map(int, input().split())) for i in range(N)]

    nodes = [Node() for i in range(M)]
    peaple = [Node() for i in range(N)]

    for i in range(N):
        l = kl[i][1:]
        peaple[i].is_root = False
        peaple[i].parent = nodes[l[0]-1]
        for j in range(1, len(l)):
            unite(nodes[l[j]-1], nodes[l[j-1]-1])
    
    ok = True
    for i in range(1, N):
        if not same_tree(peaple[0], peaple[i]):
            ok = False
    
    if ok:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()