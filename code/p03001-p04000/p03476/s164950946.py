import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
from itertools import accumulate #list(accumulate(A))

def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, n+1):
        if is_prime[i]:
            j = 2 * i
            while j <= n:
                is_prime[j] = False
                j += i
    return is_prime 
    #table = [ i for i in range(1, n+1) if is_prime[i-1]]
    #return is_prime, table

Q = ii()
lr = li2(Q)

prime = sieve(10**5)
flag = [0]*(10**5+1)

for i in range(3, 10**5+1, 2):
    if prime[i] and prime[(i+1)//2]:
        flag[i] = 1

flag = list(accumulate(flag))

for i in range(Q):
    print(flag[lr[i][1]] - flag[lr[i][0]-1])