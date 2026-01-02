#!/usr/bin/env python3

import sys
sys.setrecursionlimit(1000000)

def main():
    n, m = map(int, input().split())
    parents = [i for i in range(n)]
    for i in range(m):
        x, y, z = map(int, sys.stdin.readline().split())
        unite(x - 1, y - 1, parents)
    uniq = {find(i, parents) for i in range(n)}
    print(len(uniq))

def unite(x, y, parents):
    px = find(x, parents)
    py = find(y, parents)
    parents[py] = px

def find(x, parents):
    if parents[x] == x:
        return x
    fx = find(parents[x], parents)
    parents[x] = fx
    return fx

if __name__ == "__main__":
    main()
