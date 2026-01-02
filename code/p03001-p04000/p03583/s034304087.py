from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
for i in range(1,3501):
    for j in range(1,3501):
        if not (4*i*j - n*j - n*i):
            continue
        tmp = (n*i*j) / (4*i*j - n*j - n*i)
        if tmp.is_integer() and tmp > 0:
            print(i,j,int(tmp))
            quit()