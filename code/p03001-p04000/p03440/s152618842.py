import sys
from collections import defaultdict
import heapq
readline = sys.stdin.readline


class UnionFind:
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False


def main():
    N, M = map(int, readline().split())
    a = list(map(int, readline().split()))
    uf = UnionFind(N)
    for _ in range(M):
        x, y = map(int, readline().split())
        uf.union(x, y)
    mins = defaultdict(list)
    for i in range(N):
        mins[uf.find(i)].append(a[i])
    if len(mins) == 1:
        return 0
    ans = 0
    others = []
    for v in mins.values():
        v.sort(reverse=True)
        ans += v.pop()
        others += v
    others.sort()
    return 'Impossible' if len(others) < len(mins) - 2 else ans + sum(others[:len(mins) - 2])

print(main())
