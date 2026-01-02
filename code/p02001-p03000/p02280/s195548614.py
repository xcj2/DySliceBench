
import sys
sys.setrecursionlimit(10 ** 7)


def resolve():
    class Node:
        def __init__(self, parent, left, right):
            self.parent = parent
            self.left = left
            self.right = right
            self.height = None

        def get_type(self):
            if self.parent == -1:
                return "root"
            elif self.left == -1 and self.right == -1:
                return "leaf"
            else:
                return "internal node"

        def get_depth(self):
            if self.parent == -1:
                return 0
            else:
                depth = 1
                t = Nodes[self.parent]
                while t.parent != -1:
                    t = Nodes[t.parent]
                    depth += 1
                return depth

        def get_height(self):
            h_left = 0
            h_right = 0
            if self.left != -1:
                h_left = Nodes[self.left].get_height() + 1
            if self.right != -1:
                h_right = Nodes[self.right].get_height() + 1
            self.height = max(h_left, h_right)
            return self.height

        def get_degree(self):
            degree = 0
            if self.left != -1:
                degree += 1
            if self.right != -1:
                degree += 1
            return degree

        def get_sigling(self):
            if self. parent == -1:
                return -1
            p = Nodes[self.parent]
            if Nodes[p.left] != self and Nodes[p.left] != -1:
                return p.left
            if Nodes[p.right] != self and Nodes[p.right] != -1:
                return p.right


    N = int(input())
    Nodes = [Node(-1, None, None) for _ in range(25)]

    for _ in range(N):
        id, left, right = map(int, input().split())
        Nodes[id].left = left
        Nodes[id].right = right
        if left != -1:
            Nodes[left].parent = id
        if right != -1:
            Nodes[right].parent = id

    for i in range(N):
        node = Nodes[i]
        print("node %d: " % i, end="")
        print("parent = %d, " % node.parent, end="")
        print("sibling = %d, " % node.get_sigling(), end="")
        print("degree = %d, " % node.get_degree(), end="")
        print("depth = %d, " % node.get_depth(), end="")
        print("height = %d, " % node.get_height(), end="")
        print(node.get_type())

if __name__ == '__main__':
    resolve()

