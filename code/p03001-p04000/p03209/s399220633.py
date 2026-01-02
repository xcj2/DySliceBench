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


def rec(n: int, x: int, a: list, p: list) -> int:
    if x <= 0:
        raise ValueError

    elif n == 0:
        return 1

    elif x == 1:
        return 0

    elif 1 < x < a[n-1] + 2:
        return rec(n-1, x-1, a, p)

    elif x == a[n-1] + 2:
        return p[n-1] + 1

    elif a[n-1] + 2 < x < 2*a[n-1] + 3:
        return p[n-1] + 1 + rec(n-1, x - a[n-1] - 2, a, p)

    elif x == 2*a[n-1] + 3:
        return 2 * p[n-1] + 1

n,x = li()
a = [1]
p = [1]

for i in range(n):
    a.append(2*a[-1]+3)
    p.append(2*p[-1]+1)

print(rec(n, x, a, p))