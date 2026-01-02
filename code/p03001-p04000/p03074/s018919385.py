# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
# list(map(int, list(input()))) # スペースがない数字リストを読み込み
import math
import fractions
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
import collections
from collections import Counter
from collections import deque
import pprint

sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
def factorization(n):
    arr = []
    temp = n
    if n == 1:
        return arr

    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

# a^n
def power(a,n,mod):
    x = 1
    while n:
        if n & 1:
            x *= a % mod
        n >>= 1
        a *= a % mod
    return x % mod

# n*(n-1)*...*(l+1)*l
def kaijo(n, l, mod):
    if n == 0:
        return 1
    a = n
    tmp = n-1
    while(tmp >= l):
        a = a*tmp%mod
        tmp -= 1
    return a

inf = 10**18
mod = 10**9+7

n,k = lr()
s = sr()
length1 = 0
tmp1 = 0
one = []
for c in s:
    if c == '1':
        tmp1+=1
    else:
        if tmp1 != 0:
            length1 += 1
            one.append(tmp1)
            tmp1 = 0
if tmp1 != 0:
    length1 += 1
    one.append(tmp1)

if length1 == 0:
    print(len(s))
    sys.exit()

zero = [0 for i in range(length1+1)]
ind = 0
while ind != n and s[ind] == '0':
    zero[0]+=1
    ind+=1
tmp0 = 0
ind0 = 1
while ind != n:
    while ind != n and s[ind] == '1':
        if tmp0 != 0:
            zero[ind0] = tmp0
            tmp0 = 0
            ind0+=1
        ind+=1
    while ind != n and s[ind] == '0':
        tmp0+=1
        ind+=1
if tmp0 != 0:
    zero[-1] = tmp0

a2 = [0 for i in range(len(zero)+1)]
a2[1] = zero[0]+one[0]
for i in range(2,len(zero)):
    a2[i] = a2[i-1]+zero[i-1]+one[i-1]
a2[len(zero)] = a2[len(zero)-1]+zero[len(zero)-1]

def sumArea(l,r):
    if l == 0:
        return a2[r]-a2[l]
    else:
        return a2[r]-a2[l]+one[l-1]

if len(zero)-k+1 < 1:
    print(len(s))
    sys.exit()
ans = 0
for i in range(len(zero)-k+1):
    ans = max(ans, sumArea(i,i+k))
print(ans)