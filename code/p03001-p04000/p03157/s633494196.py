import sys
input = sys.stdin.readline

def unite(node_a, node_b):
    root_a, depth_a = node_a.root()
    root_b, depth_b = node_b.root()
    if root_a == root_b:# すでに連結成分
        return
    elif depth_a >= depth_b:# aの方が深い
        root_b.is_root = False
        root_b.parent = root_a
        root_a.white += root_b.white
        root_a.black += root_b.black
    else:# bの方が深い
        root_a.is_root = False
        root_a.parent = root_b
        root_b.white += root_a.white
        root_b.black += root_a.black

class Node:
    def __init__(self, color):# color: 0:white, 1:black
        self.parent = None
        self.is_root = True
        self.white = 1 if color == 0 else 0
        self.black = 1 if color == 1 else 0
    
    def root(self):
        node = self
        depth = 0
        while not node.is_root:
            node = node.parent
            depth += 1
        return node, depth

def main():
    H, W = map(int, input().split())
    s = [input().strip() for i in range(H)]
    
    nodes = [[Node(0 if s[j][i] == "." else 1) for i in range(W)] for j in range(H)]

    for y in range(H):
        for x in range(W):
            now = s[y][x]
            for nx, ny in [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]:
                if 0 <= nx and nx < W and 0 <= ny and ny < H:
                    if s[ny][nx] != now:
                        unite(nodes[y][x], nodes[ny][nx])
    
    ans = 0
    # count_roots = 0
    for y in range(H):
        for x in range(W):
            if nodes[y][x].is_root:
                # count_roots += 1
                node = nodes[y][x]
                ans += node.white * node.black
    print(ans)
    # print(count_roots)


if __name__ == "__main__":
    main()