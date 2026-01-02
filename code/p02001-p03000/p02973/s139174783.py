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


from bisect import bisect_left

n = ni()
a = [ni() for _ in range(n)]
lists = [[] for _ in range(n)]

lasts = [-1] * n

for ai in a:
    idx = bisect_left(lasts, ai)
    lists[idx-1].append(ai)
    lasts[idx-1] = ai

ans = 0
for lasti in lasts[::-1]:
    if lasti != -1:
        ans += 1

print(ans)