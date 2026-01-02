import sys
from collections import deque

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()


class Node:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.left = self.right = self.parent = None
        self.val = 0


class SegmentTree:
    INF = 2 ** 60

    def __init__(self, size):
        self.root = Node(0, size)
        self.leaves = [None] * size

        queue = deque()
        queue.append(self.root)

        while len(queue) > 0:
            node = queue.popleft()

            if node.end - node.begin == 1:
                self.leaves[node.begin] = node
            else:
                mid = (node.begin + node.end) // 2
                node.left = Node(node.begin, mid)
                node.right = Node(mid, node.end)
                node.left.parent = node.right.parent = node
                queue.append(node.left)
                queue.append(node.right)

    def update(self, index, val):
        node = self.leaves[index]
        node.val = val
        while node.parent is not None:
            node = node.parent
            node.val = node.left.val | node.right.val

    def val(self, begin, end, node=None):
        if node is None:
            return self.val(begin, end, self.root)
        if begin <= node.begin and node.end <= end:
            return node.val
        if node.end <= begin or end <= node.begin:
            return 0
        return self.val(begin, end, node.left) | self.val(begin, end, node.right)


N = int(input())
S = list(input())
Q = int(input())
tree = SegmentTree(N)
for i, c in enumerate(S):
    tree.update(i, 1 << (ord(c) - ord('a')))
for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        i, c = query[1:]
        i = int(i) - 1
        tree.update(i, 1 << (ord(c) - ord('a')))
    else:
        l, r = map(int, query[1:])
        print(bin(tree.val(l - 1, r)).count('1'))
