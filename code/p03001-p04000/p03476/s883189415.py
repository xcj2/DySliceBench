# coding: utf-8
from bisect import bisect_left, bisect_right
def check(x):
    flag = True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            flag = False
            break
    return flag

def primes(n):  
    is_prime = [True] * (n + 1)  
    is_prime[0] = False  
    is_prime[1] = False  
    for i in range(2, int(n**0.5) + 1):  
        if not is_prime[i]:  
            continue  
        for j in range(i * 2, n + 1, i):  
            is_prime[j] = False  
    return [i for i in range(n + 1) if is_prime[i]]
def primes_plus(l):
    # l: 素数の配列
    L = []
    for p in l:
        if check((p+1)//2):
            L.append(p)
    return L
l_primes = primes(10**6)
l_primes = primes_plus(l_primes)[1:]
# print(len(l_primes))
Q = int(input())
for i in range(Q):
    ans = 0
    l, r = map(int, input().split())
    r += 1
    l_idx = bisect_left(l_primes, l)
    r_idx = bisect_left(l_primes, r)
    # print(l_idx, r_idx)
    if l == r and l_idx == r_idx and l == l_primes[l_idx]:
        print(1)
    else:
        print(r_idx - l_idx)
# print(l_primes)