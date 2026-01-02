import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import defaultdict

dic = defaultdict(int)

n, m = li()
a = list(li())
key = set()


for ai in a:
    dic[ai] += 1
    key.add(ai)

for _ in range(m):
    bi, ci = li()
    dic[ci] += bi
    key.add(ci)

res = n
ans = 0
for ki in sorted(list(key), reverse=True):
    if res - dic[ki] >= 0:
        ans += ki*dic[ki]
        res -= dic[ki]
    else:
        ans += ki*res
        res = 0

    if res == 0:
        break
print(ans)
