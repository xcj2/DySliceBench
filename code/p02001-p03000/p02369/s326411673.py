#!/usr/bin/python3

import os
import sys


def main():
    V, E = read_ints()
    G = [set() for _ in range(V)]
    for _ in range(E):
        s, t = read_ints()
        G[s].add(t)
    print(solve(V, E, G))


def solve(V, E, G):
    done = [False] * V

    def dfs(i, path):
        path.add(i)
        for j in G[i]:
            if j in path:
                return True
            if not done[j] and dfs(j, path):
                return True
        path.remove(i)
        done[i] = True
        return False

    for i in range(V):
        if not done[i] and dfs(i, set()):
            return 1

    return 0


###############################################################################
# AUXILIARY FUNCTIONS

DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


if __name__ == '__main__':
    main()

