from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = inpln(n)
sum_a = sum(a)
a.sort()
if sum_a%10:
    print(sum_a)
else:
    for i in a:
        if i%10:
            print(sum_a - i)
            break
    else:
        print(0)
