def examA():
    N = I()
    ans = N//2 + N%2
    print(ans)
    return

def examB():
    A = [LI()for _ in range(3)]
    N = I()
    B = [I()for _ in range(N)]
    grid = [[False]*3 for _ in range(3)]
    ans = "No"
    for b in B:
        for i in range(3):
            for j in range(3):
                if A[i][j]==b:
                    grid[i][j] = True
    for i in range(3):
        flag = True
        for j in range(3):
            if not grid[i][j]:
                flag = False
        if flag:
            ans = "Yes"
    for i in range(3):
        flag = True
        for j in range(3):
            if not grid[j][i]:
                flag = False
        if flag:
            ans = "Yes"
    flag = True
    for i in range(3):
        if not grid[i][i]:
            flag = False
    if flag:
        ans = "Yes"
    flag = True
    for i in range(3):
        if not grid[i][2-i]:
            flag = False
    if flag:
        ans = "Yes"
    print(ans)
    return

def examC():
    N, M = LI()
    S = [LI()for _ in range(M)]
    ans = [-1]*N
    for s,c in S:
        s -= 1
        if ans[s]!=-1:
            if ans[s]!=c:
                print(-1)
                return
        ans[s] = c
    A = ""
    if ans[0]==0 and N>=2:
        print(-1)
        return
    elif ans[0]==-1 and N>=2:
        ans[0] = 1
    for i in ans:
        if i==-1:
            A += str(0)
        else:
            A += str(i)
    print(A)
    return

def examD():
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

    N, M, K = LI()
    uf = UnionFind(N)
    B = [0]*N
    for _ in range(M):
        a, b = LI()
        B[a-1] += 1
        B[b-1] += 1
        uf.unite(a-1,b-1)
    block = []
    for _ in range(K):
        c, d = LI()
        c -= 1
        d -= 1
        if uf.same(c,d):
            B[c] += 1
            B[d] += 1
    ans = [0]*N
    check = [-1]*N
    for i in range(N):
        root = uf.find(i)
        if check[root]==-1:
            size = uf.size(root)
            check[root] = size
        else:
            size = check[root]
        ans[i] += size-1
        ans[i] -= B[i]
        if ans[i]<0:
            ans[i] = 0
    #print(check)
    print(" ".join(map(str,ans)))
    return

def examE():
    # 一点更新、区間取得
    class segment_():
        def __init__(self, A, n, segfunc, ide_ele=0):
            #####単位元######要設定0or1orinf
            self.ide_ele = ide_ele
            ####################
            self.num = 1 << (n - 1).bit_length()
            self.seg = [self.ide_ele] * 2 * self.num
            self.segfunc = segfunc
            # set_val
            for i in range(n):
                self.seg[i + self.num] = A[i]
                # built
            for i in range(self.num - 1, 0, -1):
                self.seg[i] = self.segfunc(self.seg[2 * i], self.seg[2 * i + 1])

        def update(self, k, r):
            k += self.num
            self.seg[k] = r
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

        # 値xに1加算
        def update1(self, k):
            k += self.num
            self.seg[k] += 1
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

        def updateneg1(self, k):
            k += self.num
            self.seg[k] -= 1
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

        def query(self, p, q):
            # qは含まない
            if q < p:
                return self.ide_ele
            p += self.num;
            q += self.num
            res = self.ide_ele
            while p < q:
                if p & 1 == 1:
                    res = self.segfunc(res, self.seg[p])
                    p += 1
                if q & 1 == 1:
                    q -= 1
                    res = self.segfunc(res, self.seg[q])
                p >>= 1;
                q >>= 1
            return res

    def popcnt0(n):
        c = 0
        for i in range(27):
            c += (n >> i) & 1
        return c
    N = I()
    S = SI()
    Q = I()
    a = ord('a')
    A = [0] * (N+1)
    for i in range(N):
        A[i] = 1<<(ord(S[i]) - a)
    Seg_sum = segment_(A, N+1, lambda a, b: a | b)
    ans = []
    for _ in range(Q):
        q = LSI()
        if q[0]=="1":
            cur = 1<<(ord(q[2])-a)
            Seg_sum.update(int(q[1])-1,cur)
        else:
            cur = Seg_sum.query(int(q[1])-1,int(q[2]))
            ans.append(popcnt0(cur))
            #print(cur)
    #print(A)
    for v in ans:
        print(v)
    return

def examF():
    ans = 0
    print(ans)
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
    examE()

"""

"""