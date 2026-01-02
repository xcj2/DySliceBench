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
    p = list(map(int, input().split()))

    nodes = [Node() for i in range(N)]

    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        unite(nodes[a], nodes[b])
    
    ans = 0
    for i in range(N):
        if same_tree(nodes[i], nodes[p[i]-1]):
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()