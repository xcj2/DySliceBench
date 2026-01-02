import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

# Union-Find
def root(i):
    if node_groups[i] == i:
        return i
    else:
        node_groups[i] = root(node_groups[i])
        return node_groups[i]

def same(a, b):
    return root(a) == root(b)

def size(i):
    return group_sizes[root(i)]

def unite(a, b):
    a = root(a)
    b = root(b)

    if a == b:
        return

    if group_ranks[a] < group_ranks[b]:
        group_sizes[b] += size(a)
        node_groups[a] = b
    else:
        group_sizes[a] += size(b)
        node_groups[b] = a
        if group_ranks[a] == group_ranks[b]:
            group_ranks[a] += 1


n,m,k = get_nums_l()

lines = list(map(lambda s: s.strip(), sys.stdin.readlines()))
friends = list(map(lambda s: list(map(int, s.split())), lines[:m]))
blocks = list(map(lambda s: list(map(int, s.split())), lines[m:]))


nodes = n+1
node_groups = [ i for i in range(nodes)]
group_sizes = [ 1 for _ in range(nodes)]
group_ranks = [ 0 for _ in range(nodes)]

edges = []
for f in friends:
    unite(f[0], f[1])

group_nodes = [set() for _ in range(nodes)]
for node in range(1, n+1):
    group_nodes[root(node)].add(node)

kouho = [0] * nodes
for node in range(1, n+1):
    kouho[node] = (len(group_nodes[root(node)]) -1 )
# log("kouhoA", kouho)

for fr in friends:
    kouho[fr[0]] -= 1
    kouho[fr[1]] -= 1
for bl in blocks:
    if same(bl[0], bl[1]):
        kouho[bl[0]] -= 1
        kouho[bl[1]] -= 1

print(" ".join(map(str, kouho[1:])))