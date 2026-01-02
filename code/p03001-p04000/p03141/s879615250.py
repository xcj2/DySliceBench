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
ab = [list(li()) for _ in range(n)]
ab.sort(key=lambda x: x[0] + x[1], reverse=True)

first = 0
second = 0

for i, (ai, bi) in enumerate(ab):
    if i%2 == 0:
        first += ai
    else:
        second += bi

print(first - second)