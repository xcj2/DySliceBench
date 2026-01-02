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


def divisors(m: int):
    i = 1
    div = []
    while i * i <= m:
        if m % i == 0:
            div.append(i)
            div.append(m // i)
        i += 1

    return list(set(div))

n,m = li()

divs = divisors(m)
divs.sort(reverse=True)

ans = 1
for di in divs:
    if m // di >= n:
        ans = di
        break

print(ans)