from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N = inp()
AA = inpl()
cnts = defaultdict(int)
ed = set()
for a in AA:
    cnts[a] += 1
    ed.add(a)

aa1 = [[i,0] for i in range(1,N+1)]
for e in ed:
    aa1[cnts[e]-1][1] += 1

aa2 = [0] # 種類数
aa3 = [0] # 実枚数
for t,n in aa1:
    aa2.append(aa2[-1] + n)
    aa3.append(aa3[-1] + n*t)

L = len(aa1)
tmpl_t = []
tmpl_c = []
for i,(t,n) in enumerate(aa1):
    tmp = n + aa3[i]//t
    tmp += aa2[-1] - aa2[i+1]
    tmpl_t.append(t)
    tmpl_c.append(tmp)
    # print(t,'回食べるとき，最大',tmp,'枚までいける')

tmpl_t.reverse()
tmpl_t.append(0)
tmpl_c.reverse()
# print(tmpl_t)
# print(tmpl_c)
ans = [0]*N
for i in range(1,N+1):
    idx = bisect.bisect_left(tmpl_c,i)
    if idx == 0:
        ans[i-1] = N//i
    else:
        ans[i-1] = tmpl_t[idx]

print('\n'.join(map(str,ans)))
