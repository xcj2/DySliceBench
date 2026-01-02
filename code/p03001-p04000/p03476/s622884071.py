from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

Q = inp()
cnt = [False] * (10**5+10)
table = [False] * (10**5+10)
for i in range(1,10**5+5):
    cnt[i] = is_prime(i)
for i in range(1,10**5+5):
    table[i] = i%2 and cnt[i] and cnt[(i+1)//2]
res = [0] * (10**5+5)
for i in range(10**5+4):
    tmp = 1 if table[i] else 0
    res[i+1] = res[i] + tmp
# print(res[:20])
for _ in range(Q):
    a,b = inpl()
    print(res[b+1] - res[a])