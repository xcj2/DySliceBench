import sys
from math import gcd
from collections import defaultdict

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N = I()
mod = 10**9+7
plus = defaultdict(int)
minus = defaultdict(int)
flag = defaultdict(int)
A_zero,B_zero = 0,0
zero_zero = 0
for i in range(N):
    a,b = MI()
    if a == b == 0:
        zero_zero += 1
    elif a == 0:
        A_zero += 1
    elif b == 0:
        B_zero += 1
    else:
        if a < 0:
            a,b = -a,-b
        a,b = a//gcd(a,b),b//gcd(a,b)
        if b > 0:
            plus[(a,b)] += 1
        else:
            minus[(a,b)] += 1
            flag[(a,b)] = 1

ans = 1

for a,b in plus.keys():
    ans *= pow(2,plus[(a,b)],mod)+pow(2,minus[(b,-a)],mod)-1
    ans %= mod
    flag[(b,-a)] = 0

for key in minus.keys():
    if flag[key] == 1:
        ans *= pow(2,minus[key],mod)
        ans %= mod

ans *= pow(2,A_zero,mod)+pow(2,B_zero,mod)-1
ans %= mod

ans += zero_zero-1
ans %= mod

print(ans)
