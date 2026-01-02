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
from itertools import accumulate as acc
from collections import deque, Counter
from heapq import heapify, heappop, heappush
from bisect import bisect_left
#======================================================#

def main():
    s = IS()
    n = len(s)
    t = s.replace('x', '')
    if t != t[::-1]:
        print(-1)
        return None
    l = 0
    r = n-1
    cnt = 0
    while l < r:
        if s[l] != s[r]:
            if s[l] == 'x':
                l += 1
            elif s[r] == 'x':
                r -= 1
            cnt += 1
        else:
            l += 1
            r -= 1
    print(cnt)



if __name__ == '__main__':
    main()