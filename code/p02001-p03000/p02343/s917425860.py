import sys
input = sys.stdin.readline

def same(node_a, node_b):
    if node_a.root() == node_b.root():
        return True
    else:
        return False

def unite(node_a, node_b):
    root_a = node_a.root()
    root_b = node_b.root()
    if root_a == root_b:
        return False
    if root_b.depth > root_a.depth:
        root_a, root_b = root_b, root_a
    root_b.is_root = False
    root_b.parent = root_a
    root_a.depth = max(root_a.depth, root_b.depth+1)
    return True

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
    n, q = map(int, input().split())

    nodes = [Node() for i in range(n)]

    for i in range(q):
        c, x, y = map(int, input().split())
        if c == 0:
            unite(nodes[x-1], nodes[y-1])
        else:
            if same(nodes[x-1], nodes[y-1]):
                print(1)
            else:
                print(0)

if __name__ == "__main__":
    main()
