import sys, bisect, math, itertools, string, queue, copy
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

n = inp()
al = inpl()
rui = []
for i in range(n):
    if(i == 0):
        rui.append(al[i])
    else:
        rui.append(rui[i - 1] + al[i])

ans = 0
for i in range(n):
    ans += al[i] * (rui[n - 1] - rui[i])
    ans %= mod
print(ans)
