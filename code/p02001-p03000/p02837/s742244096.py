import random as rng
import itertools as it
import collections as col
import heapq as hq
import sys
import copy as cp
import bisect
sys.setrecursionlimit(10**9)


def dump_impl(*objects):
    print(*objects, file=sys.stderr)


def dump_dummy(*objects):
    pass


dump = dump_impl if "DEBUG" in sys.argv else dump_dummy

N = int(input())
T = [None]*N
for i in range(N):
    Ai = int(input())
    T[i] = [-1]*N
    for j in range(Ai):
        xij, yij = map(int, input().split())
        dump(i, xij-1, yij)
        T[i][xij-1] = yij
dump(T)


def imply(p, q): return (not p) or q


ans = -1
for trusts in it.product([0, 1], repeat=N):
    dump(trusts)
    ok = True
    for i, trust in enumerate(trusts):
        if trust:
            for j, tij in enumerate(T[i]):
                ok = ok and imply(tij == 1, trusts[j]) and (
                    imply(tij == 0, not trusts[j]))
    if ok:
        ans = max([ans, len([i for i in trusts if i == 1])])
    dump(ans)
print(ans)
