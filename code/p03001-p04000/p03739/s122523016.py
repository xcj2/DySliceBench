from collections import Counter,defaultdict
import sys,heapq,bisect,math,itertools,string,queue,fractions
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))
def inpl_str(): return list(sys.stdin.readline().split())
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

n = inp()
a = inpl()
acc = list(itertools.accumulate(a))
#+-+-+-
cnt = 0
tmp = 0
for i in range(n):
    if i%2==0:
        tt = acc[i] + tmp
        if tt <= 0:
            cnt += 1 - tt
            tmp += 1 - tt
    else:
        tt = acc[i] + tmp
        if tt >= 0:
            cnt += tt + 1
            tmp -= tt + 1
ans = cnt
#-+-+-+
cnt = 0
tmp = 0
for i in range(n):
    if i%2:
        tt = acc[i] + tmp
        if tt <= 0:
            cnt += 1 - tt
            tmp += 1 - tt
    else:
        tt = acc[i] + tmp
        if tt >= 0:
            cnt += tt + 1
            tmp -= tt + 1
    # print(i,cnt,tmp,tt)
print(min(ans,cnt))