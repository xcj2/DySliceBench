from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
c = []
s = []
f = []
for i in range(n-1):
    a,b,z = inpl()
    c.append(a)
    s.append(b)
    f.append(z)

for i in range(n):
    if i == n-1:
        print(0)
        break
    tmp = s[i] + c[i]
    for j in range(i+1,n-1):
        if tmp <= s[j]:
            tmp = s[j] + c[j]
        elif (tmp - s[j]) % f[j] == 0:
            tmp = tmp + c[j]
        else:
            tmp = (tmp//f[j]+1)*f[j] + c[j]
    print(tmp)