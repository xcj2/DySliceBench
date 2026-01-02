def ABC106_B():
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        # divisors.sort()
        return divisors
    N = I()
    ans = 0
    for i in range((N+1)//2):
        cur = i*2+1
        if len(make_divisors(cur))==8:
            ans += 1
    print(ans)
    return

def ABC122_B():
    S = SI()
    ans = 0
    cur = 0
    d = {"A","C","G","T"}
    for s in S:
        if s in d:
            cur += 1
        else:
            ans = max(ans,cur)
            cur = 0
    ans = max(ans,cur)
    print(ans)
    return

def paken2019_C():
    N, M = LI()
    A = [LI()for _ in range(N)]
    T = [i for i in range(M)]
    ans = 0
    for t1,t2 in itertools.permutations(T,2):
        cur = 0
        for i in range(N):
            cur += max(A[i][t1],A[i][t2])
        ans = max(ans,cur)
    print(ans)
    return

def ABC95_C():
    A, B, C, X, Y = LI()
    if A+B<=C*2:
        ans = A*X+B*Y
    else:
        if X>Y:
            ans = Y*C*2 + min(A,C*2)*(X-Y)
        else:
            ans = X*C*2 + min(B,C*2)*(Y-X)
    print(ans)
    return

def SMTB_D():
    def flag(n,s):
        for l in range(n,N):
            if S[l]==str(s):
                return l
        return N
    N = I()
    S = SI()
    ans = 0
    for i in range(10):
        L1 = flag(0,i)
        for j in range(10):
            L2 = flag(L1+1,j)
            for k in range(10):
                L3 = flag(L2+1,k)
                if L3<N:
                    ans += 1
                    #print(i,j,k)
    print(ans)
    return

def JOI2007_3():
    N = I()
    V = [LI() for _ in range(N)]
    D = set()
    for vx,vy in V:
        D.add((vx,vy))
    ans = 0
    for i in range(N):
        a1, b1 = V[i]
        for j in range(i+1,N):
            a2, b2 = V[j]
            va, vb = a2 - a1, b2 - b1
            if (a1 + vb, b1 - va) in D and (a2 + vb, b2 - va) in D:
                ans = max(ans, va ** 2 + vb ** 2)
            if (a1 - vb, b1 + va) in D and (a2 - vb, b2 + va) in D:
                ans = max(ans, va ** 2 + vb ** 2)
    print(ans)
    return
"""
10
9 4
4 3
1 1
4 2
2 4
5 8
4 0
5 3
0 5
5 2
"""# 10

def square869120Contest():
    def length(a,b,x,y):
        if x>y:
            x,y = y,x
        rep = 0
        if a<x:
            rep += (x-a)*2
        if y<b:
            rep += (b-y)*2
        rep += (y-x)
        return rep
    N = I()
    AB = [LI()for _ in range(N)]
    ans = inf
    for i in range(N):
        s = AB[i][0]
        for j in range(N):
            g = AB[j][1]
            cur = 0
            for k in range(N):
                cur += length(AB[k][0],AB[k][1],s,g)
            ans = min(ans,cur)
    print(ans)
    return

def JOI7_D():
    M = I()
    S = [LI()for _ in range(M)]
    Ss = [(0,0)]
    curx,cury = S[0]
    for sx,sy in S[1:]:
        Ss.append((sx-curx,sy-cury))
        curx = sx; cury = sy
    #print(Ss)
    N = I()
    X = [LI()for _ in range(N)]
    D = set()
    for i in range(N):
        cur = (X[i][0],X[i][1])
        D.add(cur)
    for i in range(N):
        flag = True
        curx, cury = X[i]
        for k in range(M):
            curx += Ss[k][0]
            cury += Ss[k][1]
            #print(curx,cury)
            if not (curx, cury) in D:
                flag = False
                break
        if flag:
            #print(i,X[i])
            ansx = X[i][0] - S[0][0]
            ansy = X[i][1] - S[0][1]
            print(ansx,ansy)
            return
    return

def ABC128_C():
    N, M = LI()
    S = [[]for _ in range(N)]
    for i in range(M):
        s = LI()
        for j in s[1:]:
            S[j-1].append(i)
    P = LI()
    #print(S)
    loop = 2**N
    ans = 0
    for i in range(loop):
        p = [0]*M
        cur = []
        for j in range(N):
            if (1<<j)&i==(1<<j):
                cur.append(j)
        for k in cur:
            for l in S[k]:
                p[l] += 1
        flag = True
        for j in range(M):
            if p[j]%2!=P[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)
    return

def ABC2_D():
    N, M = LI()
    V = set()
    for _ in range(M):
        x,y = LI()
        V.add((x,y))
    loop = 2**N
    ans = 0
    #print(V)
    for i in range(loop):
        cur = []
        for j in range(N):
            if (1<<j)&i==(1<<j):
                cur.append(j+1)
        flag = True
        for k1,k2 in itertools.permutations(cur,2):
            if not ((k1,k2) in V or (k2,k1) in V):
                flag = False
                break
        if flag:
            ans = max(ans,len(cur))
    print(ans)
    return

def JOI7_E():
    R, C = LI()
    A = [LI()for _ in range(R)]
    loop = 2**R
    ans = 0
    for i in range(loop):
        rev = set()
        for j in range(R):
            if (1<<j)&i==(1<<j):
                rev.add(j)
        cur = 0
        for j in range(C):
            s = 0
            for k in range(R):
                if k in rev and A[k][j]==0:
                    s += 1
                elif (not k in rev) and A[k][j]==1:
                    s += 1
            cur += max(s,R-s)
        ans = max(ans,cur)
    print(ans)
    return

def square869120Contest4_B():
    N, K = LI()
    A = LI()
    ans = inf
    loop = 2**(N-1)
    for i in range(loop):
        look = set()
        for j in range(N-1):
            if (1<<j)&i==(1<<j):
                look.add(j+1)
        if len(look)<K-1:
            continue
        high = A[0]
        cur = 0
        flag = True
        for j in range(1,N):
            if not (j in look):
                if A[j]>high:
                    flag = False
                    break
            else:
                if high >= A[j]:
                    cur += (high - A[j] + 1)
                    high += 1
                else:
                    high = A[j]
        #print(look,cur)
        if not flag:
            continue
        ans = min(ans,cur)
    print(ans)
    return

def ABC145_C():
    N = I()
    X = [LI()for _ in range(N)]
    ans = 0
    c = 0
    for x in itertools.permutations(X):
        cur = 0
        c += 1
        for i in range(N-1):
            cur += ((x[i+1][0]-x[i][0])**2 + (x[i+1][1]-x[i][1])**2)**0.5
        ans += cur
    ans /= c
    print(ans)
    return

def ABC150_C():
    N = I()
    T = [i+1 for i in range(N)]
    P = LI()
    Q = LI()
    for i,t in enumerate(itertools.permutations(T)):
        flag_P = True
        flag_Q = True
        for j in range(N):
            if t[j]!=P[j]:
                flag_P = False
            if t[j]!=Q[j]:
                flag_Q = False
        if flag_P:
            a = i
        if flag_Q:
            b = i
    ans = abs(a-b)
    print(ans)
    return

def JOI2009_2():
    d = I()
    N = I()
    M = I()
    D = [I()for _ in range(N-1)]
    K = [I()for _ in range(M)]
    D.append(0)
    D.sort()
    D.append(d)
    ans = 0
    for i in range(M):
        cur = bisect.bisect_right(D,K[i])
        ans += min(K[i]-D[cur-1],D[cur]-K[i])
    print(ans)
    return
"""
20 
4 
4 
12
8 
16 
7 
7 
11 
8
"""#3

def ARC37_C():
    N, K = LI()
    A = LI()
    B = LI()
    B.sort()
    l = 0; r = inf
    while(r-l>1):
        cur = 0
        now = (l+r)//2
        for a in A:
            if a==0:
                cur += N
            else:
                cur += bisect.bisect_right(B,now//a)
        if cur<K:
            l =now
        else:
            r = now
    ans = r
    print(ans)
    return

def ABC27_D():
    def judge(h):
        D = [0]*N
        for i in range(N):
            if h<H[i][0]:
                return False
            cur = (h-H[i][0])//H[i][1]
            if cur>=N:
                cur = N-1
            D[cur] += 1
        s = 0
        #print(D,h)
        for i in range(N):
            s += D[i]
            if s>i+1:
                return False
        return True
    N = I()
    H = [LI()for _ in range(N)]
    l = 0; r = inf
    while(r-l>1):
        now = (l+r)//2
        if judge(now):
            r = now
        else:
            l = now
    ans = r
    print(ans)
    return

def JOI2008_3():
    N, M = LI()
    P = [I()for _ in range(N)]
    P_2 = set()
    for i in range(N+1):
        if i==N:
            p1 = 0
        else:
            p1 = P[i]
        for j in range(N+1):
            if j==N:
                p2 = p1
            else:
                p2 = p1+P[j]
            P_2.add(p2)
    P_2 = list(P_2)
    P_2.sort()
    ans = 0
    for p2 in P_2:
        if M<p2:
            continue
        cur = P_2[bisect.bisect_right(P_2,M-p2)-1]+p2
        ans = max(ans,cur)
    print(ans)
    return
"""
3 21 
16 
11 
2
"""#20

def ABC138_D():
    def bfs(n,edges,s,C):
        W = [-1]*n
        que = deque()
        que.append(s)
        W[s] = C[s]
        rep = W[s]
        while(que):
            now = que.pop()
            nowW = W[now]
            for i in edges[now]:
                if W[i]==-1:
                    que.append(i)
                    W[i] = nowW + C[i]
                    rep += W[i]
        return W
    N, Q = LI()
    V = [[]for _ in range(N)]
    for _ in range(N-1):
        a,b = LI()
        a -= 1; b -= 1
        V[a].append(b)
        V[b].append(a)
    C = [0]*N
    for _ in range(Q):
        p,x = LI()
        C[p-1] += x
    ans = bfs(N,V,0,C)
    print(" ".join(map(str,ans)))
    return


import sys,copy,bisect,itertools,heapq,math,random
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    ABC138_D()

"""
3 21 
16 
11 
2
"""#20