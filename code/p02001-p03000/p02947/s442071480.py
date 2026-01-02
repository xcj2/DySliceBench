from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

def conb(n,r): 
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n = inp()
s = []
for i in range(n):
    tmp = list(input())
    s.append(sorted(tmp))
s.sort()
# print(s)
cnt = []
tmp = 0
for i in range(n-1):
    if s[i] == s[i+1]:
        tmp += 1
    elif tmp != 0:
        cnt.append(tmp)
        tmp = 0
if tmp != 0:
    cnt.append(tmp)
# print(cnt)
res = 0
for i in cnt:
    res += conb(i+1, 2)
print(res)