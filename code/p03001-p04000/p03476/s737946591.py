from collections import Counter,defaultdict
import sys,heapq,bisect,math,itertools,string,queue
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def conb(n,r): return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

q = inp()
L = [0] * q
R = [0] * q
for i in range(q):
    L[i],R[i] = inpl()
    L[i] = (L[i]+1)//2
    R[i] = (R[i]+1)//2
# print(L,R)
cnt = [0] * ((10**5+10)//2)
for i in range(1,(10**5+5)//2):
    if is_prime(i) and is_prime(i+i-1):
        cnt[i] = cnt[i-1] + 1
    else:
        cnt[i] = cnt[i-1]
for i in range(q):
    print(cnt[R[i]] - cnt[L[i]-1])