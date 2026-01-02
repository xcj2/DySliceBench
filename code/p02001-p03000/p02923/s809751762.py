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

n = ni()
h = list(li())

ans = 0
tmp = 0
nex = h[-1]

for hi in h[-2::-1]:
    if hi >= nex:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 0

    nex = hi

print(max(ans, tmp))