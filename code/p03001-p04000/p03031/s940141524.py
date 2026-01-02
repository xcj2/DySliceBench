import sys
input = sys.stdin.readline
from itertools import combinations

def readlines(n):
    for _ in range(n):
        k, *s = map(int, input().split())
        yield s

def on(s, p, comb):
    return len([s_ for s_ in s if s_ in comb]) % 2 == p

def main():
    n, m = map(int, input().split())
    switches = list(range(1, n+1))
    S = list(readlines(m))
    P = list(map(int, input().split()))
    for i in range(n+1):
        for comb in combinations(switches, i):
            if all(on(s, p, set(comb)) for s, p in zip(S, P)):
                yield 1

print(sum(main()))

