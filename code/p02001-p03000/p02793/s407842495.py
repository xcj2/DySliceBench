from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())


def gcd(a,b):
	while b:
		a,b = b, a%b
	return a

def lcm(a,b):
	return a*b // gcd(a,b)


N = inp()
aa = inpl()
tmp = 1

for a in aa:
    tmp = lcm(a,tmp)

tmp %= mod
ans = 0
for a in aa:
    ans += tmp * pow(a,mod-2,mod)
    ans %= mod

print(ans)
