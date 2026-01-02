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
    def __init__(self, key, left=None, right=None):
        self.val = key
        self.left = left
        self.right = right


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def preorder(root):
    ret = []
    if root is None: return ret
    ret.append(root.val)
    ret.extend(preorder(root.left))
    ret.extend(preorder(root.right))
    return ret


def inorder(root):
    ret = []
    if root is None: return ret
    ret.extend(inorder(root.left))
    ret.append(root.val)
    ret.extend(inorder(root.right))
    return ret


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    s, key = sl()
    root = BinaryNode(int(key))

    for n in range(N - 1):
        input = sl()
        if input[0] == 'print':
            print("", *inorder(root))
            print("", *preorder(root))
        else:
            insert(root, BinaryNode(int(input[1])))


if __name__ == '__main__':
    main()

