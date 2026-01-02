#!/usr/bin/env pypy3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import math
from collections import defaultdict
pc = True
n = int(input())
a = list(map(int,input().split()))
g = math.gcd(a[0],a[1])
for i in range(2,n):
    g = math.gcd(g,a[i])
M = max(a)

LIMIT=max(a)
minPrime = [0]*(LIMIT+1)
minPrime[1] = 1
def make():
    for i in range(2,LIMIT+1):
        if minPrime[i] == 0:
            minPrime[i] = i
            #print(i)
            for j in range(i+i,LIMIT+1,i):
                #print(i,j)
                if minPrime[j] == 0:
                    minPrime[j] = i
make()
class Sieve_of_Eratosthenes:
    def __init__(self, N):
        self.sieve = [-1] * (N+1)

        for i in range(2,N+1):
            if self.sieve[i] == -1:
                for j in range(1,1+N//i):
                    self.sieve[i*j] = i

    def isprime(self, num):
        if num <= 1:
            return False
        else:
            return self.sieve[num] == num

    def factorization(self, num):
        ret = set([])
        while num != 1:
            div = self.sieve[num]
            ret.add(div)
            num //= div
        return ret

def factrial(N):
    ret = set()
    while 1 != N:
        ret.add(minPrime[N])
        N = N//minPrime[N]
    if N != 1:
        ret.add(N)
    return ret


sofe = Sieve_of_Eratosthenes(M)
ddic = defaultdict()
judge = set([])

for i in a:
    if not pc:
        break
    #asf = sofe.factorization(i)
    asf = factrial(i)

    if judge & asf != set():
        pc = False
    judge |= asf
if pc:
    print("pairwise coprime")
elif g == 1:
    print("setwise coprime")
else:
    print("not coprime")
# import sys,collections

# N = int(sys.stdin.readline())
# #a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = list(map(int,input().split()))

# import math

# # def factrial(N):
# #     ret = []
# #     while minPrime[N] != N:
# #         ret.append(minPrime[N])
# #         N = N//minPrime[N]
# #     if N != 1:
# #         ret.append(N)
# #     return ret

# def factrial(N):
#     ret = set()
#     while 1 != N:
#         ret.add(minPrime[N])
#         N = N//minPrime[N]
#     if N != 1:
#         ret.add(N)
#     return ret

# for i in range(N):
#     acc = math.gcd(acc,a[i])
# if acc != 1:
#     print("not coprime")
#     exit()

# pairwise = True
# p = set() #all prime
# for e in a:
#     if not pairwise:
#         break
#     f = factrial(e)
#     if p & f != set():
#         pairwise = False
#         print("setwise coprime")
#         exit(0)
#     p = p | f

# if pairwise:
#     print("pairwise coprime")
# else:
#     print("setwise coprime")
