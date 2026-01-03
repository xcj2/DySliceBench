from collections import defaultdict
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


n, k = LI()
d = defaultdict(int)
for _ in range(n):
    a, b = LI()
    d[a] += b

d = sorted(d.items(), key=lambda x: x[0])
# print(d)
i = 0
ans = 1
cnt = 0
while cnt < k:
    ans = d[i][0]
    cnt += d[i][1]
    i += 1
print(ans)
