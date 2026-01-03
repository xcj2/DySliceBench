#!/usr/bin/env python3

from itertools import permutations

class Graph:
    def __init__(self, n_nodes):
        self.adj = [set() for i in range(n_nodes)]

    def add_edge(self, a1, b1):
        self.adj[a1 - 1].add(b1)
        self.adj[b1 - 1].add(a1)

    def are_adj(self, a1, b1):
        return b1 in self.adj[a1 - 1]

def main():
    n, m = map(int, input().split())
    gr = Graph(n)
    for i in range(m):
        a, b = map(int, input().split())
        gr.add_edge(a, b)
    paths = all_permutations_from_one(n)
    cnt = 0
    for p in paths:
        if is_possible(p, gr):
            cnt += 1
    print(cnt)

def all_permutations_from_one(n):
    perms_2_n = list(permutations(range(2, n + 1)))
    perms_1_n = [(1,) + p2n for p2n in perms_2_n]
    return perms_1_n

def is_possible(path, gr):
    l = len(path)
    flag = True
    for i in range(l - 1):
        a, b = path[i:i + 2]
        if not gr.are_adj(a, b):
            flag = False
    return flag

main()
