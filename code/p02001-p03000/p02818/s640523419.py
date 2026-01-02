def ABC120_D():
    class UnionFind():
        def __init__(self, n):
            self.parent = [-1 for _ in range(n)]
            # 正==子: 根の頂点番号 / 負==根: 連結頂点数

        def find(self, x):
            # 要素xが属するグループの根を返す
            if self.parent[x] < 0:
                return x
            else:
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

        def unite(self, x, y):
            # 要素xが属するグループと要素yが属するグループとを併合する
            x, y = self.find(x), self.find(y)
            if x == y:
                return False
            else:
                if self.size(x) < self.size(y):
                    x, y = y, x
                self.parent[x] += self.parent[y]
                self.parent[y] = x

        def same(self, x, y):
            # 要素x, yが同じグループに属するかどうかを返す
            return self.find(x) == self.find(y)

        def size(self, x):
            # 要素xが属するグループのサイズ（要素数）を返す
            x = self.find(x)
            return -self.parent[x]

        def is_root(self, x):
            # 要素の根をリストで返す
            return self.parent[x] < 0

        def roots(self):
            # すべての根の要素をリストで返す
            return [i for i, x in enumerate(self.parent) if x < 0]

        def members(self, x):
            # 要素xが属するグループに属する要素をリストで返す
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def group_count(self):
            # グループの数を返す
            return len(self.roots())

        def all_group_members(self):
            # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
            return {r: self.members(r) for r in self.roots()}
    N, M = LI()
    P = [[]for _ in range(M)]
    for i in range(M):
        P[i] = LI()
    uf = UnionFind(N)
    ans = [N*(N-1)//2]*M
    for i,[a,b] in enumerate(P[M-1:0:-1]):
        #print(i,a,b)
        a -= 1; b -= 1
        if uf.same(a,b):
            ans[i+1] = ans[i]
        else:
            cur = uf.size(a)*uf.size(b)
            ans[i+1] = ans[i]-cur
            uf.unite(a,b)
    for v in ans[::-1]:
        print(v)
    return

def JOI8_1():
    N = I()
    C = [I()for _ in range(N)]
    prev = C[0]
    BW = [[1,prev]]
    for i in range(1,N):
        #print(BW)
        if BW[-1][1]==C[i]:
            BW[-1][0] += 1
        else:
            if i%2==0:
                BW.append([1,C[i]])
            else:
                if len(BW) > 1:
                    BW[-2][0] += (BW[-1][0] + 1)
                    del BW[-1]
                else:
                    BW[0][0] += 1
                    BW[0][1] = C[i]
    ans = 0
    #print(BW)
    for i,s in BW:
        if s==0:
            ans += i
    print(ans)
    return
"""
8
1
0
1
1
0
0
0
1
"""
def JOI13_A():
    N = I()
    A = LI()
    S = []
    cur = 1
    prev = A[0]
    for i in range(1,N):
        if prev^A[i]==1:
            cur += 1
        else:
            S.append(cur)
            cur = 1
        prev = A[i]
    if cur>0:
        S.append(cur)
    #print(S)
    ans = 0
    for i in range(len(S)-2):
        cur = S[i]+S[i+1]+S[i+2]
        if ans<cur:
            ans = cur
    if len(S)<=2:
        ans = N
    print(ans)
    return
"""
10 
1 1 0 0 1 0 1 1 1 0
"""
def square869120Contest5_B():
    def length(a,b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
    def check(r):
        for i in range(M):
            for j in range(N):
                if length(X[i],A[j][0:2])<A[j][2]+r+_ep:
                    return False
            for j in range(M):
                if i==j:
                    continue
                if length(X[i],X[j])<r+r+_ep:
                    return False
        return True
    N, M = LI()
    A = [LI()for _ in range(N)]
    X = [LI()for _ in range(M)]
    minA = inf
    for i,j,a in A:
        if minA>a:
            minA = a
    l = 0; r = 200
    while(r-l>_ep):
        now = (l+r)/2
        if check(now):
            l = now
        else:
            r = now
    ans = min(l,minA)
    print(ans)
    return

def ABC144_D():
    a, b, x = LI()
    half = a*a*b/2
    if x>=half:
        y = (half*2-x)/(a*a/2)
        deg = math.atan2(a,y)
        #print(y,a,deg)
        ans = 90-deg*180/math.pi
    else:
        y = x/(a*b/2)
        deg = math.atan2(b,y)
        ans = deg*180/math.pi
    print(ans)
    return

def square869120Contest3_B():
    def check_del(S):
        sco = 0
        for h in range(H):
            for w in range(W-K+1):
                s = S[h][w]
                if s==0:
                    continue
                if K==3 and s==S[h][w+1] and s==S[h][w+2]:
                    d = 3
                    for k in range(W-K+1-w):
                        if S[h][w]!=S[h][w+2+k]:
                            break
                        d += 1
                    t = S[h][w]
                    sco += cal_score(t,d)
                    del_stone(S,h,w,d)
                elif K==2 and s==S[h][w+1]:
                    d = 2
                    for k in range(W-K-w):
                        if S[h][w]!=S[h][w+2+k]:
                            break
                        d += 1
                    t = S[h][w]
                    sco += cal_score(t,d)
                    del_stone(S,h,w,d)
        return sco,S
    def del_stone(S,y,x,k):
        for i in range(k):
            S[y][x+i] = 0
        return S
    def cal_score(t,c):
        return (2**now)*(t*c)
    def move_stone(S):
        rep = deepcopy(S)
        for w in range(W):
            blank = -1
            que = deque()
            for h in range(H)[::-1]:
                if rep[h][w]==0:
                    if blank==-1:
                        blank = h
                else:
                    if blank>=0:
                        que.append(rep[h][w])
                        rep[h][w] = 0
            if blank==-1:
                continue
            for h,i in enumerate(que):
                rep[blank-h][w] = i
        return rep
    H, W, K = LI()
    A = [SI()for _ in range(H)]
    C = [[]for _ in range(H)]
    for h in range(H):
        for w in range(W):
            C[h].append(int(A[h][w]))
    if K>=4:
        print(0)
        return
    ans = 0
    if K==1:
        for c in C:
            ans += sum(c)
        print(ans)
        return
    for h in range(H):
        for w in range(W):
            nowC = deepcopy(C)
            nowC[h][w] = 0
            #print(nowC)
            cur = 0
            now = 0
            while(True):
                nowC = move_stone(nowC)
                #print(nowC)
                rep,nowC = check_del(nowC)
                #print(nowC)
                #print()
                if rep==0:
                    break
                cur += rep
                now += 1
            #print(h,w,cur)
            if ans<cur:
                ans = cur
    print(ans)
    return

def ABC149_B():
    A, B, K = LI()
    if A>=K:
        print(A-K,B)
    elif A+B>=K:
        print(0,A+B-K)
    else:
        print(0,0)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
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

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    ABC149_B()
"""

"""
