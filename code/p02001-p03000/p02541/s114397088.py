import sys
input = sys.stdin.buffer.readline
import math

# 素因数分解、辞書で返すやつ
# mathをimportする
def prime(n):
    factor = {}
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            if not num in factor.keys():
                factor[num] = 1
            else:
                factor[num] += 1
        if num > n:
            break
    if n != 1:
        if not n in factor.keys():
            factor[n] = 1
        else:
            factor[n] += 1
    return factor

# (x, y) of ax + by = 1
def oneOfSolution(a, b):
    if b == 1:
        return 0, 1
    d = a//b
    p, q = oneOfSolution(b, a%b)
    return q, p-d*q

def solution(a, b):
    if b > a:
        y0, x0 = oneOfSolution(b, a)
    else:
        x0, y0 = oneOfSolution(a, b)
    x = x0%b
    if a*x < 2:
        x += b
    return a*x-1

N = int(input())

if N == 1:
    ans = 1
else:
    N_prime = prime(N)
    W = []
    for num, cnt in N_prime.items():
        if num == 2:
            W.append(num**(cnt+1))
        else:
            W.append(num**cnt)

    M = len(W)
    ans = N
    for bit in range(1<<M):
        a = 1; b = 1
        for i, m in enumerate(W):
            if bit&(1<<i):
                a *= m
            else:
                b *= m
        ans = min(ans, solution(a, b))

print(ans)