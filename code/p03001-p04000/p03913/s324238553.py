def examA():
    H, W = LI()
    S = [LSI() for _ in range(H)]
    Alpha = [chr(ord('A') + i) for i in range(26)]
    for i in range(H):
        for j in range(W):
            if S[i][j]=="snuke":
                ans = str(Alpha[j]) + str(i+1)
    print(ans)
    return

def examB():
    N = I()
    ans = []
    cur = int((N*2-1)**0.5)+1
    ansC = (cur+1)*cur//2
    neg = ansC-N
    if neg>cur:
        cur -=1
        ansC = (cur + 1) * cur // 2
        neg = ansC - N
    for i in range(1,cur+1):
        if i!=neg:
            ans.append(i)
    for v in ans:
        print(v)
#    print(cur,neg)
    return

def bfs(n,e,fordfs):
    #点の数、スタートの点、有向グラフ
    que = deque()
    que.append(e)
    len = [10**9]*n
    len[e] = 0
    while que:
        now = que.popleft()
        nowlen = len[now]
        for ne in fordfs[now]:
            if len[ne] == 10**9:
                len[ne] = nowlen+1
                que.append(ne)
    return len
def examC():
    N, M = LI()
    V = [[]for _ in range(N+M)]
    for i in range(N):
        L = LI()
        for k in range(1,L[0]+1):
            V[i].append(L[k]+N-1)
            V[L[k]+N-1].append(i)
    length = bfs(N+M,0,V)
    ans = "YES"
    for i in length[:N]:
        if i==10**9:
            ans = "NO"
    print(ans)
    return

def examD():
    N, M = LI()
    X = LI(); maxX = max(X)+1
    dx = defaultdict(int)
    dm = [set()for _ in range(M)]
    d = defaultdict(int)
    for x in X:
        dx[x] +=1
        d[x%M] +=1
        dm[x%M].add(x)
    ans = 0
#    print(d); print(dx); print(dm)
    ans +=d[0]//2
    d[0] = 0
    for i in range(1,1+M//2):
        cur = min(d[i],d[M-i])
        ans +=cur
        d[i] -=cur; d[M-i] -=cur
#    print(ans); print(d)
    for i in d.keys():
        for j in dm[i]:
            cur = min(dx[j]//2,d[i]//2)
            d[i] -= cur * 2
            ans += cur
            if d[i]<=1:
                break
    print(ans)
    return

def caneat(x,A,n):
    cur = n - A*x
    if cur<=0:
        return 1
    l = cur//(x+1); r = cur%(x+1)
    if l==0:
        return 1
    now = pow(l,(x-r+1))*pow((l+1),r)
    return now
def ternarySearch(A,n,e):
    #何回喰うか
    fr, to = 0, e
    while to - fr > 2:
        x1, x2 = (2 * fr + to)//3, (2 * to + fr)//3
        f1, f2 = caneat(x1,A,n), caneat(x2,A,n)
        if f1 > f2:
            to = x2
        elif f1 < f2:
            fr = x1
        else:
            fr, to = x1, x2
    return max(caneat(fr,A,n),caneat(fr+1,A,n),caneat(to,A,n))
def examE():
    N, A = LI()
    l = 0; r = N+1
    while(r-l>1):
        now = (l+r)//2
        maxE = min(40,now//(A+1))
        cur = ternarySearch(A,now,maxE)
        if N<=cur:
            r = now
        else:
            l = now
#        print(l,r,cur)
#    print(l,r)
    ans = r
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examE()
