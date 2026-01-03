#!/usr/bin/env python3

import sys

graph = {}

def solve(start, visited = set()):
    global graph

    visited = visited | set([start])
    if len(visited) == len(graph):
        return 1

    ans = 0
    for next_ in graph[start]:
        if not next_ in visited:
            ans += solve(next_, visited)
    return ans

def read_int_list():
    return [int(s) for s in sys.stdin.readline().rstrip().split(" ")]

def dprint(*args, **kwargs):
    return
    print(*args, **kwargs)

def connect(f, t):
    global graph
    if not f in graph:
        graph[f] = set()
    graph[f].add(t)

def main():
    global graph
    
    _, m = read_int_list()
    for _ in range(0, m):
        a, b = read_int_list()
        connect(a, b)
        connect(b, a)

    dprint(repr(graph))
    print(solve(1))

main()