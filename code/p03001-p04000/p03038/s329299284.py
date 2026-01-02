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

n, m = li()
a = list(li())

dic = defaultdict(int)

for ai in a:
    dic[ai] += 1

for _ in range(m):
    b, c = li()
    dic[c] += b

keys = sorted(list(dic.keys()), reverse=True)

rest = n
ans = 0
for ki in keys:
    if dic[ki] > rest:
        ans += ki * rest
        rest = 0

    elif dic[ki] == rest:
        ans += ki * dic[ki]
        rest = 0

    else:
        ans += ki * dic[ki]
        rest -= dic[ki]

    if rest <= 0:
        break

print(ans)
