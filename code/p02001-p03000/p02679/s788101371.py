import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

def f(a,b):
    if a == 0:
        return 0,1
    if b == 0:
        return 1,0
    f = math.gcd(a,b)
    return a//f, b//f

N = I()
A,B = LIR(N,2)

beki = [1]*(N+1)
for i in range(1,N+1):
    beki[i] = beki[i-1]*2
    beki[i] %= mod


dplus = defaultdict(int)
dplus2 = defaultdict(int)
dminus = defaultdict(int)
dminus2 = defaultdict(int)
dzeros = defaultdict(int)

zero = 0
both_zero = 0
for i in range(N):
    if A[i] == 0 and B[i] == 0:
        both_zero += 1
    elif A[i] == 0 or B[i] == 0:
        a,b = f(abs(A[i]),abs(B[i]))
        dzeros[(a,b)] += 1
    else:
        if A[i]*B[i] > 0:
            a,b = f(abs(A[i]),abs(B[i]))
            dplus[(a,b)] += 1
            dplus2[(a,b)] += 1
        else:
            a,b = f(abs(A[i]),abs(B[i]))
            dminus[(b,a)] += 1
            dminus2[(b,a)] += 1

ans = 1
count = 0

for k in dplus.keys():
    if dminus[k]:
        temp = beki[dplus[k]] + beki[dminus[k]] - 1
        ans *= temp
        ans %= mod
    else:
        count += dplus[k]

for k in dminus2.keys():
    if dplus2[k]:
        continue
    else:
        count += dminus2[k]

temp = beki[dzeros[(0,1)]] + beki[dzeros[(1,0)]] -1
ans *= temp
ans %= mod

ans *= beki[count]
ans -= 1
ans += both_zero
ans %= mod
print(ans)