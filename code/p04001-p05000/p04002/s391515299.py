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

h, w, n = li()
dic = defaultdict(int)

drs = [-1, 0, 1]
dcs = [-1, 0, 1]

ans = [0]*10
ans[0] = (h-2)*(w-2)

for _ in range(n):
    a, b = li_()
    for dr in drs:
        for dc in dcs:
            if 0 < a+dr < h-1 and 0 < b+dc < w-1:
                dic[(a+dr, b+dc)] += 1

for _, val in dic.items():
    ans[val] += 1
    ans[0] -= 1

print(*ans, sep="\n")