#!/usr/bin/python3

import math
import os
import sys


sys.setrecursionlimit(1000000)


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, M, E):
    G = [set() for _ in range(N)]
    for a, b in E:
        G[a].add(b)

    visited = set()
    stk = []
    stki = {}

    def dfs(i):
        if i in visited:
            return

        stki[i] = len(stk)
        stk.append(i)

        for j in G[i]:
            if j in visited:
                continue
            if j in stki:
                si = stki[j]
                vset = set(stk[si:])
                loopd = {}
                for k in range(si, len(stk) - 1):
                    loopd[stk[k]] = stk[k + 1]
                loopd[stk[-1]] = stk[si]
                return slim_loop(vset, loopd)
            result = dfs(j)
            if result:
                return result

        stk.pop()
        del stki[i]
        visited.add(i)
        return None

    def slim_loop(vset, loopd):
        i = next(iter(vset))
        endi = i
        while True:
            jset = G[i] & vset
            if len(jset) > 1:
                oj = loopd[i]
                for j in jset:
                    if j == oj or j not in vset:
                        continue
                    k = loopd[i]
                    while k != j:
                        vset.remove(k)
                        k = loopd[k]
                    loopd[i] = j
                endi = i

            i = loopd[i]
            if i == endi:
                break

        return vset

    for i in range(N):
        if i not in visited:
            result = dfs(i)
            if result:
                return result

    return None


def main():
    N, M = [int(e) for e in inp().split()]
    E = []
    for _ in range(M):
        a, b = [int(e) - 1 for e in inp().split()]
        E.append((a, b))

    result = solve(N, M, E)
    if not result:
        print('-1')
    else:
        print(len(result))
        for v in result:
            print(v + 1)


if __name__ == '__main__':
    main()
