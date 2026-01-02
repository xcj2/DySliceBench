###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

N, P = mi()

def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

flist = factorize(P)

ans = 1 #絶対1以上
for fctr, nowcnt in flist:
  if nowcnt//N >= 1:
    ans *= (fctr ** (nowcnt//N))

print(ans)

