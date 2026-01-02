import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.is_root = True
        self.parent = None
        self.child_num = 0
    
    def root_node(self):
        node = self
        while not node.is_root:
            node = node.parent
        return node

def main():
    N, M = map(int, input().split())

    nodes = [Node() for i in range(N)]

    ab = [list(map(int, input().split())) for i in range(M)]
    
    inc = (N * (N-1)) // 2
    ans = [inc]
    for i in range(M-1, -1, -1):
        a, b = ab[i]
        a -= 1
        b -= 1
        root_a = nodes[a].root_node()
        if root_a != nodes[a]:
            nodes[a].parent = root_a
        root_b = nodes[b].root_node()
        if root_b != nodes[b]:
            nodes[b].parent = root_b
        if root_a == root_b:# もともと連結成分だった場合
            ans.append(inc)
        else:# 新たに連結成分になった場合
            if root_b.child_num > root_a.child_num:
                tmp = root_a
                root_a = root_b
                root_b = tmp
            inc -= (root_a.child_num + 1) * (root_b.child_num + 1)
            ans.append(inc)
            root_b.is_root = False
            root_b.parent = root_a
            root_a.child_num += root_b.child_num + 1

    for i in range(M-1, -1, -1):
        print(ans[i])

if __name__ == "__main__":
    main()

