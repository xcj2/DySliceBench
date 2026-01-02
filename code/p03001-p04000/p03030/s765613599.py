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
shop = []
order = {}
for i in range(n):
    s,p = ls()
    p = int(p)
    shop.append([s,p])
    order[(s,p)] = i

ans = sorted(sorted(shop, key=lambda x: x[1], reverse=True), key=lambda x:x[0])


for i, (name, point) in enumerate(ans):
    print(order[(name, point)] + 1)
    order[(name, point)] = i
