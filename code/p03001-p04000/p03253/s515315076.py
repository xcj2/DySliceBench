from collections import deque
from heapq import heapify,heappop,heappush,heappushpop
from copy import copy,deepcopy
from itertools import permutations,combinations
from collections import defaultdict,Counter
# from math import gcd,ceil,floor,factorial
# from fractions import gcd
from functools import reduce
from pprint import pprint

def myinput():
    return map(int,input().split())

def mylistinput(n):
    return [ list(myinput()) for _ in range(n) ]

def mycol(data,col):
    return [ row[col] for row in data ]

def mysort(data,col):
    data.sort(key=lambda x:x[col],reverse=False)
    return data

def mymax(data):
    M = -1*float("inf")
    for i in range(len(data)):
        m = max(data[i])
        M = max(M,m)
    return M

def mymin(data):
    m = float("inf")
    for i in range(len(data)):
        M = min(data[i])
        m = min(m,M)
    return m

def myoutput(ls,space=True):
    if space:
        if len(ls)==0:
            print(" ")
        elif type(ls[0])==str:
            print(" ".join(ls))
        elif type(ls[0])==int:
            print(" ".join(map(str,ls)))
        else:
            print("Output Error")
    else:
        if len(ls)==0:
            print("")
        elif type(ls[0])==str:
            print("".join(ls))
        elif type(ls[0])==int:
            print("".join(map(str,ls)))
        else:
            print("Output Error")

n,m = myinput()
mod = 10**9 + 7

if m==1:
    print(1)
    exit()

# 素因数分解
def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

table = prime_decomposition(m)
# print(table)

# """nを素因数分解"""
# """2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
def factorization(n):
    arr = []
    temp = n
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
# print(factorization(m))
## [[2, 3], [3, 1]] 
##  24 = 2^3 * 3^1

# Combinations
def comb_mod_faster(n,k,mod):
    if n<k:
        return 0
    if n<0 or k<0:
        return 0
    k = min(n-k,k)
    ans = 1
    inv = [1]*(k+1)
    if k>=1:
        ans *= (n-k+1)%mod
    for i in range(2,k+1):
        inv[i] = mod - inv[mod%i]*(mod//i)%mod
        ans = ans*(n-k+i)*inv[i]%mod
    return ans

# Repeated Combinations
def repeated_combinations(n,k,mod):
    return comb_mod_faster(n+k-1,k,mod)

f = factorization(m)

ans = 1
for i in range(len(f)):
    k = f[i][1]
    ans *= repeated_combinations(n,k,mod)
print(ans%mod)