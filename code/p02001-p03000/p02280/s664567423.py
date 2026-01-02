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


def get_depth(parent, node):
    depth = 0
    n = node
    while True:
        if parent[n] == -1: break
        n = parent[n]
        depth += 1

    return depth


def get_sibling(parent, tree, node):
    p = parent[node]
    if p == -1:
        return -1
    else:
        return tree[p][0] if tree[p][0] != node else tree[p][1]


def get_degree(tree, node):
    l, r = tree[node]
    ret = 0
    if l != -1: ret += 1
    if r != -1: ret += 1
    return ret


def get_height(tree, node):
    h1, h2 = 0, 0
    if tree[node][0] != -1:
        h1 = get_height(tree, tree[node][0]) + 1
    if tree[node][1] != -1:
        h2 = get_height(tree, tree[node][1]) + 1
    return max(h1, h2)


def get_type(parent, tree, node):
    type = ''
    if parent[node] == -1:
        type = 'root'
    elif tree[node][0] == -1 and tree[node][1] == -1:
        type = 'leaf'
    else:
        type = 'internal node'
    return type


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    parent = [-1] * N
    tree = collections.defaultdict(list)

    for n in range(N):
        id, l, r = il()
        tree[id] = [l, r]
        if l != -1:
            parent[l] = id
        if r != -1:
            parent[r] = id

    for node in range(N):
        print('node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}'.format(
            node, parent[node], get_sibling(parent, tree, node), get_degree(tree, node), get_depth(parent, node),
            get_height(tree, node), get_type(parent, tree, node)
        ))


if __name__ == '__main__':
    main()

