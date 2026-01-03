import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
from functools import partial, reduce
from operator import mul
prod = partial(reduce, mul)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()
from collections import Counter

fibo = [1, 1]
for i in range(2, 9):
    fibo.append(fibo[i - 1] + fibo[i - 2])

def main():
    n = II()
    S = []
    for _ in range(n):
        S.append(SI())
    cnt = Counter(S[0])
    for s in S[1:]:
        s = Counter(s)
        for x in cnt.keys():
            cnt[x] = min(cnt[x], s[x])
        cnt = +cnt
    ans = ''
    for k, v in sorted(list(cnt.items())):
        ans += k * v
    return ans

print(main())