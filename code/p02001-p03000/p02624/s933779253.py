import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()

import math

def sieve_of_eratosthenes(n):
    prime_list = []  # n以下の素数のリスト
    A = [1]*(n+1)    # A[i] = iが素数なら1,その他は0
    A[0] = A[1] = 0
    for i in range(2,math.floor(math.sqrt(n))+1):
        if A[i]:
            prime_list.append(i)
            for j in range(i**2,n+1,i):
                A[j] = 0
    for i in range(math.floor(math.sqrt(n))+1,n+1):
        if A[i] == 1:
            prime_list.append(i)
    return prime_list

primelist = sieve_of_eratosthenes(N)

list = [i for i in range(N+1)]

for p in primelist:
    a = p
    r = 2
    while a <= N:
        for i in range(1,N//a+1):
            if i % p == 0:
                continue
            else:
                list[a*i] *= r
        a *= p
        r += 1

print(sum(list))