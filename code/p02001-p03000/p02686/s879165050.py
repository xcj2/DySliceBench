def examA():
    S = SI()
    T = SI()
    if S==T[:len(S)]:
        if len(S)+1==len(T):
            print("Yes")
            return
    print("No")
    return

def examB():
    A, B, C, K = LI()
    ans = 0
    if A>=K:
        ans = K
    else:
        ans += A
        K -= A
        if K>B:
            K -= B
            ans -= K
    print(ans)
    return

def examC():
    N, M, X = LI()
    C = [LI()for _ in range(N)]
    loop = 2**N
    ans = inf
    for l in range(loop):
        cur = 0
        A = [0]*M
        for j in range(N):
            if (1<<j)&l>0:
                cur += C[j][0]
                for k in range(M):
                    A[k] += C[j][k+1]
        flag = True
        for i in range(M):
            if A[i]<X:
                flag = False
                break
        if flag:
            ans = min(ans,cur)
    if ans==inf:
        print(-1)
        return
    print(ans)
    return

def examD():
    N, K = LI()
    A = LI()
    locat_doubling = [[0]*N for _ in range(100)]
    for i in range(N):
        locat_doubling[0][i] = i
        locat_doubling[1][i] = A[i]-1
    for k in range(2,100):
        for i in range(N):
            locat_doubling[k][i] = locat_doubling[k-1][locat_doubling[k-1][i]]
    #print(locat_doubling)
    ans = [i for i in range(N)]
    for k in range(100):
        for i in range(N):
            if K&(1<<k)>0:
                ans[i] = locat_doubling[k+1][ans[i]]
    print(ans[0]+1)
    return

def examE():
    class combination():
        # 素数のmod取るときのみ　速い
        def __init__(self, n, mod):
            self.n = n
            self.mod = mod
            self.fac = [1] * (n + 1)
            self.inv = [1] * (n + 1)
            for j in range(1, n + 1):
                self.fac[j] = self.fac[j - 1] * j % mod

            self.inv[n] = pow(self.fac[n], mod - 2, mod)
            for j in range(n - 1, -1, -1):
                self.inv[j] = self.inv[j + 1] * (j + 1) % mod

        def comb(self, n, r):
            if r > n or n < 0 or r < 0:
                return 0
            return self.fac[n] * self.inv[n - r] * self.inv[r] % self.mod
    N, M, K = LI()
    C = combination(N,mod2)
    ans = 0
    for i in range(N):
        if i>K:
            break
        cur = C.comb(N-1,i) * M * pow((M - 1), N - i - 1, mod2) % mod2
        #print(cur)
        ans += cur
        ans %= mod2
    print(ans)
    return

def examF():
    N = I()
    LRC = [[0,0,0]for _ in range(N)]
    flag_l = False; flag_r = False
    C = 0
    for i in range(N):
        S = SI()
        cur = 0
        l = 0
        for s in S:
            if s==")":
                cur += 1
            else:
                cur -= 1
            if cur>l:
                l = cur
        LRC[i][0] = l
        if l==0:
            flag_l = True
        cur = 0
        r = 0
        for s in S[::-1]:
            if s=="(":
                cur += 1
            else:
                cur -= 1
            if cur>r:
                r = cur
        LRC[i][1] = r
        if r==0:
            flag_r = True
        LRC[i][2] = l-r
        C += l-r
    if (not flag_l) or (not flag_r):
        print("No")
        return
    if C!=0:
        print("No")
        return
    #print(LRC)
    LRC.sort(key=lambda x:x[1])
    A = [0]*N
    B = [0]*N
    #print(LRC)
    for i in range(N):
        A[i] = LRC[i][2]
        B[i] = LRC[i][0]
    now = 0
    for i in range(N):
        ne = bisect.bisect_right(B,now)-1
        now += A[ne]
        #print(now,ne)
        A[ne] = 0
    if random.random()>0.5:
        print("No")
        return
    print("Yes")
    return

def examF2():
    N = I()
    LC = []
    RC = []
    C = 0
    for i in range(N):
        S = SI()
        cur = 0
        l = 0
        for s in S:
            if s==")":
                cur += 1
            else:
                cur -= 1
            if cur>l:
                l = cur
        cur = 0
        r = 0
        for s in S[::-1]:
            if s=="(":
                cur += 1
            else:
                cur -= 1
            if cur>r:
                r = cur
        cnt = l-r
        C += cnt
        if cnt<0:
            LC.append((l,r))
        else:
            RC.append((r,l))
    if C!=0:
        print("No")
        return
    LC.sort()
    RC.sort()
    #print(LC)
    #print(RC)
    L = 0
    for nowl,nowr in LC:
        if nowl>L:
            print("No")
            #print(nowl,nowr)
            return
        L += nowr-nowl
    R = 0
    for nowr,nowl in RC:
        if nowr>R:
            print("No")
            #print(nowr,nowl,RC,R)
            return
        R += nowl-nowr
    print("Yes")
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
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

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examF2()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn

5
))))(((((
(((
))))))((
)((
)

6
(()))(())(((
()((()
())
)(()()(
)))(())(((
))))()
"""