def examA():
    N = DI()/dec(7)
    ans = N
    print(N)
    return

def examB():
    ans = 0
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    # 参考 (https://qiita.com/b1ueskydragon/items/41cec5d36c747f73d515)
    def KMP(S, word):
        def partial_match_table(word):
            table = [0] * (len(word) + 1)
            table[0] = -1
            i, j = 0, 1

            while j < len(word):
                matched = word[i] == word[j]

                if not matched and i > 0:
                    i = table[i]
                else:
                    if matched:
                        i += 1
                    j += 1
                    table[j] = i

            return table

        table = partial_match_table(word)
        # print(table)
        i, p = 0, 0
        match = []
        while (i < len(S) and p < len(word)):
            # print(i,p)
            if S[i] == word[p]:
                i += 1;
                p += 1
                if p == len(word):
                    match.append(i - p)
                    p = table[p]
            else:
                if p == 0:
                    i += 1
                else:
                    p = table[p]

        return match

    class UnionFind():
        def __init__(self, n):
            self.parent = [-1 for _ in range(n)]
            # 正==子: 根の頂点番号 / 負==根: 連結頂点数

        def reset(self):
            self.parent = [-1] * len(self.parent)

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

    S = SI()
    T = SI()
    if len(S)<len(T):
        S *= (len(T)//len(S))+1
    #print(S)
    N = len(S)
    n = len(T)
    V = [[]for _ in range(N)]
    S *= 2
    kmp = KMP(S,T)
    #print(kmp)

    for i in kmp:
        if i>=N:
            continue
        V[i%N].append((i+n)%N)
    uf = UnionFind(N)
    #print(V)

    def dfs(s):
        cnt = 0
        for v in V[s]:
            # 一回見た中に自身が含まれている
            if uf.same(s,v):
                return -1
            # すでに一回は見た頂点の場合
            if uf.size(v)>1:
                #print("test",s,uf.size(v))
                cnt = uf.size(v)
                uf.unite(s, v)
                return cnt
            else:
                uf.unite(s, v)
                child = dfs(v)
            if child==-1:
                return -1
            cnt = child+1
        return cnt

    ans = 0
    for i in range(N):
        if uf.size(i)!=1:
            continue
        cur = dfs(i)
        #print(cur,i)
        if cur==-1:
            print(-1)
            return
        if ans<cur:
            ans = cur
    print(ans)
    return

from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(2*10**6)

if __name__ == '__main__':
    examF()

"""
abababababc
babababa
"""