import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

def diff(node_a, node_b):
    root_a, cost_a = node_a.root(0)
    root_b, cost_b = node_b.root(0)
    if root_a == root_b:
        return True, cost_a - cost_b
    else:
        return False, cost_a - cost_b

def merge(node_a, node_b, weight):
    root_a, cost_a = node_a.root(0)
    root_b, cost_b = node_b.root(0)
    root_a.weight = weight + cost_b - cost_a
    root_a.is_root = False
    root_a.parent = root_b

class Node:
    def __init__(self):
        self.is_root = True
        self.parent = None
        self.weight = 0
    
    def root(self, cost):
        if self.is_root:
            return self, cost
        root, max_ = self.parent.root(cost + self.weight)
        self.parent = root
        self.weight = max_ - cost
        return root, max_

def main():
    n, q = map(int, input().split())
    
    nodes = [Node() for i in range(n)]

    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 0:
            x, y, z = query[1:]
            if not diff(nodes[x], nodes[y])[0]:
                merge(nodes[x], nodes[y], z)
        else:
            x, y = query[1:]
            jud, ans = diff(nodes[x], nodes[y])
            if jud:
                print(ans)
            else:
                print("?")

if __name__ == "__main__":
    main()
