import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

class union_find():
    def __init__(self, n):
        self.nodes = n
        self.node_groups = [ i for i in range(n)]
        self.group_sizes = [ 1 for _ in range(n)]
        self.group_ranks = [ 0 for _ in range(n)]

    def root(self, i):
        if self.node_groups[i] == i:
            return i
        else:
            self.node_groups[i] = self.root(self.node_groups[i])
            return self.node_groups[i]

    def same(self, a, b):
        return self.root(a) == self.root(b)

    def size(self, i):
        return self.group_sizes[self.root(i)]

    def unite(self, a, b):
        a = self.root(a)
        b = self.root(b)

        if a == b:
            return

        if self.group_ranks[a] < self.group_ranks[b]:
            self.group_sizes[b] += self.size(a)
            self.node_groups[a] = b
        else:
            self.group_sizes[a] += self.size(b)
            self.node_groups[b] = a
            if self.group_ranks[a] == self.group_ranks[b]:
                self.group_ranks[a] += 1


def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    n,m = get_nums_l()

    uf = union_find(n)

    for i in range(m):
        a,b = get_nums_l()
        a-=1
        b-=1
        uf.unite(a,b)
    
    groups = len(set([ uf.root(i) for i in range(n) ]))

    print(groups-1)

main()