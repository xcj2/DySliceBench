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

def linear_nCk(n,k):
    a = [1]*(k+1)
    for i in range(1,k+1):
        a[i] = a[i-1]*(n-k+i)//i
    return a[-1]

N,P = LI()
A = LI()

odd = 0
even = 0
for i in range(N):
    if A[i]%2 == 0:
        even += 1
    else:
        odd += 1

if P == 0:
    ans = 0
    for i in range(0,odd+1,2):
        ans += linear_nCk(odd,i)
    ans = ans*(2**even)
    print(ans)
else:
    ans = 0
    for i in range(1,odd+1,2):
        ans += linear_nCk(odd,i)
    ans = ans*(2**even)
    print(ans)