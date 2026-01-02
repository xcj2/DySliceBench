import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

def make_prime_list(lower: int, upper: int) -> list:
    if upper <= 2:
        return []
    
    prime_list = []
    
    is_prime = [True]*upper
    is_prime[0] = False
    is_prime[1] = False
    
    n = 2
    while n**2 < upper:
        if is_prime[n]:
            res = 2*n
            while res < upper:
                is_prime[res] = False
                res += n
                
        n += 1
        
    for i in range(lower, upper):
        if is_prime[i]:
            prime_list.append(i)
            
    return prime_list

def is_like2017(num: int, prime_set) -> int:
    if num in prime_set and (num+1)//2 in prime_set:
        return 1
    else:
        return 0

from itertools import accumulate

MAX_N = 10**5+1

prime_list = make_prime_list(1,MAX_N)
prime_set = set(prime_list)

prime_cnt = [0]*MAX_N

for i in range(1,MAX_N,2):
    prime_cnt[i] += is_like2017(i, prime_set)
        
prime_cum = list(accumulate(prime_cnt))


q = ni()
for _ in range(q):
    l,r = li()
    print(prime_cum[r] - prime_cum[l-1])