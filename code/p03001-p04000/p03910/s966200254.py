from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
cnt = 0
i = 1
if n == 1:
    print(1)
    quit()
elif n == 2:
    print(2)
    quit()
while True:
    cnt += i
    if cnt >= n:
        break
    i += 1
res = []
while n > 0:
    res.append(i)
    n -= i
    i -= 1
    if n > i:
        continue
    res.append(n)
    break
for i in range(len(res))[::-1]:
    print(res[i])