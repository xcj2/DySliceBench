import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
## dp ##
def DD2(d1,d2,init=0): return [[init]*d2 for _ in range(d1)]
def DD3(d1,d2,d3,init=0): return [DD2(d2,d3,init) for _ in range(d1)]
## math ##
def to_bin(x: int) -> str: return format(x, 'b') # rev => int(res, 2)
def to_oct(x: int) -> str: return format(x, 'o') # rev => int(res, 8)
def to_hex(x: int) -> str: return format(x, 'x') # rev => int(res, 16)
MOD=10**9+7
def divc(x,y) -> int: return -(-x//y)
def divf(x,y) -> int: return x//y
def gcd(x,y):
    while y: x,y = y,x%y
    return x
def lcm(x,y): return x*y//gcd(x,y)
def enumerate_divs(n):
    """Return a tuple list of divisor of n"""
    return [(i,n//i) for i in range(1,int(n**0.5)+1) if n%i==0]
def get_primes(MAX_NUM=10**3):
    """Return a list of prime numbers n or less"""
    is_prime = [True]*(MAX_NUM+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(MAX_NUM**0.5)+1):
        if not is_prime[i]: continue
        for j in range(i*2, MAX_NUM+1, i):
            is_prime[j] = False
    return [i for i in range(MAX_NUM+1) if is_prime[i]]
## libs ##
from itertools import accumulate as acc, combinations as combi, product, combinations_with_replacement as combi_dup
from collections import deque, Counter
from heapq import heapify, heappop, heappush
from bisect import bisect_left
#======================================================#

def main():
    n, m = MII()
    ab = [MIIZ() for _ in range(m)]
    cnt = 0
    for i in range(m):
        graph = [[] for _ in range(n)]
        for k,(a,b) in enumerate(ab):
            if i == k: continue
            graph[a].append(b)
            graph[b].append(a)
        dist = [-1]*n
        dq = deque()
        dist[0] = 0
        dq.append(0)
        while dq:
            v = dq.popleft()
            for nv in graph[v]:
                if dist[nv] != -1: continue
                dist[nv] = dist[v] + 1
                dq.append(nv)
        if -1 in dist:
            cnt += 1
    print(cnt)



if __name__ == '__main__':
    main()