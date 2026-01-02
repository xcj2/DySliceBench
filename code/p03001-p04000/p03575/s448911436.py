# coding:utf-8

import sys
from collections import deque, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n, m = LI()
edge = [LI() for _ in range(m)]


def dfs(s):
    q = deque([s])
    visited = set()

    while q:
        curr = q.pop()
        visited.add(curr)
        for next in G[curr]:
            if next in visited:
                continue
            q.append(next)

    return True if len(visited) == n else False


ans = 0
for i in range(m):
    G = defaultdict(list)
    for j, e in enumerate(edge):
        if i == j:
            continue
        a, b = e
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    ans += 0 if dfs(0) else 1

print(ans)
