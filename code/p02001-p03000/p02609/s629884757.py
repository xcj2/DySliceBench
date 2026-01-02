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

N = I()
X = list(input())

# xが0になるまで何回かかるか
def calc(x):
    n = len(x)
    c = x.count('1')
    now = 0
    for i in range(n):
        if x[i] == '1':
            now += 2**(n-1-i)
            now %= c
    if now == 0:
        return 1
    else:
        return calc(list(format(now,'b')))+1

count = X.count('1')

a = [1]*(N+1)
if count >= 2:
    a[0] = 1%(count-1)
    for i in range(1,N+1):
        a[i] = a[i-1]*2
        a[i] %= count-1

b = [1]*(N+1)
b[0] = 1%(count+1)
for i in range(1,N+1):
    b[i] = b[i-1]*2
    b[i] %= count+1

suma = 0
sumb = 0
for i in range(N):
    if X[i] == '1':
        suma += a[N-i-1]
        sumb += b[N-i-1]
        sumb %= (count+1)
        if count >= 2:
            suma %= (count-1)

ans = [0]*N
for i in range(N):
    if X[i] == '1':
        if count == 1:
            ans[i] = 0
            continue
        val = (suma-a[N-i-1])%(count-1)
        if val == 0:
            ans[i] = 1
        else:
            ans[i] = calc(list(format(val,'b')))+1
    else:
        val = (sumb+b[N-i-1])%(count+1)
        if val == 0:
            ans[i] = 1
        else:
            ans[i] = calc(list(format(val,'b')))+1

for a in ans:
    print(a)