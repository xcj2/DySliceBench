import sys, os, math, bisect, itertools, collections, heapq, queue, copy, array

# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
# from decimal import Decimal
# from collections import defaultdict, deque

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


class BinaryNode:
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, N):
        self.tree = [-1] * N
        self.parent = [-1] * N

    def insert_node(self, N, node):
        self.tree[N] = node
        if node.left is not None:
            self.parent[node.left] = N
        if node.right is not None:
            self.parent[node.right] = N

    def get_root(self):
        for n in range(len(self.parent)):
            if self.parent[n] == -1:
                return n

    def preorder(self, N):
        ret = [N]
        if self.tree[N].left is not None:
            ret.extend(self.preorder(self.tree[N].left))
        if self.tree[N].right is not None:
            ret.extend(self.preorder(self.tree[N].right))
        return ret

    def inorder(self, N):
        ret = []
        if self.tree[N].left is not None:
            ret.extend(self.inorder(self.tree[N].left))
        ret.append(N)
        if self.tree[N].right is not None:
            ret.extend(self.inorder(self.tree[N].right))
        return ret

    def postorder(self, N):
        ret = []
        if self.tree[N].left is not None:
            ret.extend(self.postorder(self.tree[N].left))
        if self.tree[N].right is not None:
            ret.extend(self.postorder(self.tree[N].right))
        ret.append(N)
        return ret


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    tree = BinaryTree(N)
    for n in range(N):
        n, left, right = il()
        if left == -1: left = None
        if right == -1: right = None
        tree.insert_node(n, BinaryNode(n, left, right))
    print('Preorder')
    print('', *tree.preorder(tree.get_root()))
    print('Inorder')
    print('', *tree.inorder(tree.get_root()))
    print('Postorder')
    print('', *tree.postorder(tree.get_root()))


if __name__ == '__main__':
    main()

