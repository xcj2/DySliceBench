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

n, k = li()
a = list(li())

ans = 1

# aの和を素因数分解
divs = divisors(sum(a))
divs.sort(reverse=True)

# 大きい順に判定
for div in divs:
    if div == 1:
        break

    amodr = [ai % div for ai in a]
    amodr.sort(reverse=True)
    rsum = sum(amodr)
    rnum = rsum // div

    req = rsum - sum(amodr[:rnum])

    if req <= k:
        ans = div
        break

print(ans)
