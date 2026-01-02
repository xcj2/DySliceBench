import math
def is_prime(n):
    if n == 1: return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True
def near2017(n):
    if is_prime(n):
        return is_prime((n+1)//2)
    else:
        return False
#############################################################
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')

N = 100000
prime = [0]*100001
cur = 0
ans = []
for i in range(1,N+1):
    if near2017(i):
        cur +=1
        prime[i] = cur
    else:
        prime[i] = prime[i-1]
#print(prime[N])
cur = int(0)
Q = I()
for i in range(Q):
    l, r = LI()
    cur = prime[r] - prime[l-1]
    ans.append(cur)

for v in ans:
    print(v)
