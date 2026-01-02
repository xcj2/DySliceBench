import sys
input = sys.stdin.readline
from itertools import combinations
from operator import contains

def readlines(n):
    for _ in range(n):
        x, y = input().split()
        yield int(x)-1, y=="1"

def main():
    n = int(input())
    asserts = []

    for _ in range(n):
        a = int(input())
        asserts.append(list(readlines(a)))

    def check(comb):
        for i in comb:
            for x, y in asserts[i]:
                mujun = contains if not y else lambda a, b: b not in a
                if mujun(comb, x):
                    return -1
        
        return len(comb)

    for i in range(1, n+1):
        for comb in combinations(range(n), i):
            yield check(set(comb))

    yield 0

print(max(main()))