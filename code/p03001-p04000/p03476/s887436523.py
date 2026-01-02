import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

Q = I()
lr = [LI() for i in range(Q)]

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
    for i in range(math.floor(math.sqrt(n)),n+1):
        if A[i] == 1:
            prime_list.append(i)
    return A

prime = sieve_of_eratosthenes(10**5)
prime_like_2017 = [0]*(10**5+1)
prime_like_2017[3] = 1

for i in range(3,10**5+1):
    if prime[i] == 0:
        continue
    elif i == 2:
        continue
    elif i == 3:
        prime_like_2017[i] = 1
    elif i % 4 == 3:
        continue
    else:
        if prime[(i+1)//2] == 1:
            prime_like_2017[i] = 1

from itertools import accumulate

P = list(accumulate(prime_like_2017))  # P[i] = iまでに2017に似た数が何個あるか

for i in range(Q):
    print(P[lr[i][1]]-P[lr[i][0]-1])