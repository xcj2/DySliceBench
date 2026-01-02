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
a = list(li())
x = [0]*n

xsum = sum(a) // 2
x[0] = xsum - sum(a[1::2])

for i in range(1, n):
    x[i] = a[i-1] - x[i-1]

print(*list(map(lambda y: 2*y, x)))