from collections import Counter,defaultdict,deque
from heapq import heapify,heappop,heappush
import sys,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

def check(i,j):
    for k in range(m):
        for l in range(m):
            if a[i+k][j+l] != b[k][l]:
                return False
    return True

n,m = inpl()
a = []
b = []
for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())

bb = True
for i in range(n-m+1):
    for j in range(n-m+1):
        if check(i,j):
            print('Yes')
            quit()
print('No')