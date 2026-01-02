from collections import Counter,defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

ans = []
n = inp()
a = inpl()
aa = set(a)
aa = sorted(list(aa),reverse=True)
# print(a,aa)
d = defaultdict(int)

for key in a:
    d[key] += 1
for i in aa:
    if d[i] >= 4:
        if ans == []:
            print(i**2)
            quit()
    if d[i] >= 2:
        ans.append(i)
        if len(ans) == 2:
            print(ans[0]*ans[1])
            quit()
print(0)