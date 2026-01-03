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
    N = int(input())
    
    nodes = [Node() for i in range(N)]

    # 各町の座標をタプル(i, x, y)に入れて配列に格納
    xy = []
    for i in range(N):
        x, y = map(int, input().split())
        xy.append((i, x, y))
    
    # 使う可能性のある辺のみを取り出す
    edges = []
    xy = sorted(xy, key=lambda x: x[1])# x座標昇順
    # print("x:", xy)
    for i in range(1, N):
        edges.append((xy[i][1] - xy[i-1][1], xy[i-1][0], xy[i][0]))
    xy = sorted(xy, key=lambda x: x[2])# y座標昇順
    # print("y:", xy)
    for i in range(1, N):
        edges.append((xy[i][2] - xy[i-1][2], xy[i-1][0], xy[i][0]))
    
    ans = 0
    edges = sorted(edges)
    # print(edges)
    for (cost, a, b) in edges:
        if not same_tree(nodes[a], nodes[b]):
            unite(nodes[a], nodes[b])
            ans += cost
    print(ans)




if __name__ == "__main__":
    main()