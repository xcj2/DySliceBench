import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9+7

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

# nC0~nCn odd or even
def nCk(n):
    num = [0]*(n+1)
    for i in range(n+1):
        now = 2
        while now <= i:
            num[i] += i//now
            now *= 2
    #cumnum = [num[0]]
    #for i in range(1,n+1):
    #    cumnum.append(cumnum[-1]+num[i])
    ret = [0]*(n+1)
    for i in range(n+1):
        if num[n] > num[i]+num[n-i]:
            ret[i] = 0
        else:
            ret[i] = 1
    return ret

N = I()

A = list(input())
a = [0]*N
for i in range(N):
    a[i] = int(A[i])

b = [0]*(N-1)
for i in range(N-1):
    b[i] = abs(a[i]-a[i+1])

flag = False
for i in range(N-1):
    if b[i] == 1:
        flag = True
        break

nlist = nCk(N-2)

ans = 0
if not flag:
    for i in range(N-1):
        ans += nlist[i]*b[i]
        ans %= 4
    print(ans)
    #raise(ValueError)
else:
    for i in range(N-1):
        ans += nlist[i]*(b[i]%2)
        ans %= 2
    print(ans)
    #raise(ValueError)