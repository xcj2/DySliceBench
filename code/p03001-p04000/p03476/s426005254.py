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
n = 10**5+10
Q = inp()
ch = [False] * (n+5)
for i in range(1,n):
    if is_prime(i):
        ch[i] = True
table = [0] * (n+5)
for i in range(1,n):
    tmp = 0
    if i%2 and ch[i] and ch[(i+1)//2]:
        tmp = 1
    table[i] = table[i-1] + tmp
for _ in range(Q):
    a,b = inpl()
    print(table[b] - table[a-1])