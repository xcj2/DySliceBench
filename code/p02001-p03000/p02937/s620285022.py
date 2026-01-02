from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

S = input()
T = input()

ALPs = defaultdict(list)

for i,s in enumerate(S):
    ALPs[s].append(i+1)

Ls = [len(ALPs[chr(i)]) for i in range(97,97+28)]


itr = 0
cnt = 0 # 周回数
for t in T:
    L = Ls[ord(t)-97]
    if L == 0:
        print(-1)
        exit()
    else:
        ind = bisect.bisect_right(ALPs[t],itr)
        if ind == L:
            itr = ALPs[t][0]
            cnt += 1
        else:
            itr = ALPs[t][ind]
        #print(ALPs[t],ind,itr)


ans = cnt*len(S) + itr

print(ans)
