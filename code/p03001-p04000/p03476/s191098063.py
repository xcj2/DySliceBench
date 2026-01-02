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

Q = ii()
lr = li2(Q)
from collections import deque
que = deque()

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime = [0]*(10**5+1)
flag = [0]*(10**5+1)
prime[2] = 1

for i in range(3, 10**5+1, 2):
    if is_prime(i):
        prime[i] = 1

for i in range(3, 10**5+1, 2):
    if prime[i] and prime[(i+1)//2]:
        flag[i] = 1

ans = list(accumulate(flag))

for i in range(Q):
    print(ans[lr[i][1]]-ans[lr[i][0]-1])