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

def make_divisors(n,sort=False):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    if sort:
        divisors.sort()
    return divisors

N,K = LI()

numl = [0]*(K+1)

ans = 0
for i in range(1,K+1)[::-1]:
    num = pow(math.floor(K/i),N,mod)
    for j in range(2*i,K+1,i):
        num -= numl[j]
        num %= mod
    numl[i] = num
    ans += num*i
    ans %= mod

print(ans)