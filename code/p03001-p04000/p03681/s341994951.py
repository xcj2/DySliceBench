from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

def nnn(a):
    res = 1
    for i in range(1,a+1):
        res *= i
        res %= mod
    return res

n,m = inpl()
if n == m:
    print((nnn(n) **2 *2)%mod)
elif abs(n-m) == 1:
    print((nnn(n) * nnn(m))%mod)
else:
    print(0)     
