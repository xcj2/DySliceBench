inf = float("inf")

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def input_int():return int(input())
def input_ints():return map(int,input().split())
def input_ints_list():return list(input_ints())
def input_str():return input()
def input_strs():return input().split()
def input_lines(n,f):return [f() for _ in range(n)]

import importlib
def import_module(name):return importlib.import_module(name)

def gcd_base(a,b):return import_module('fractions').gcd(a,b) # 最大公約数（2値)
def gcd(a):return import_module('functools').reduce(gcd_base,a) # 最大公約数（リスト）
def lcm_base(a,b):return (a*b)//gcd_base(a,b) # 最小公倍数(2値)
def lcm(a):return import_module('functools').reduce(lcm_base,a,1) # 最小公倍数(リスト)

def permutations(a,n):return import_module('itertools').permutations(a,n) # 順列
def combinations(a,n):return import_module('itertools').combinations(a,n) # 組み合わせ
def product(a,b):return import_module('itertools').product(a,b) # 二つのリストの直積

def init_array_1dim(v,n):return [v]*n
def init_array_2dim(v,n,m):return [init_array_1dim for _ in range(m)]

# 四捨五入はround
def ceil(a):return import_module('math').ceil(a) # 切り上げ
def floor(a):return import_module('math').floor(a) # 切り捨て

# キュー
def init_q(a):return import_module('collections').deque(a)
def q_pop(a):return a.popleft()
def q_push(a,v):a.appendleft(v)
def q_pushlist(a,l):a.extendleft(l)
def q_append(a,v):a.append(v)
def q_appendlist(a,l):a.extend(l)

# プライオリティキュー
def init_heap(a):import_module('heapq').heapify(a)
def heap_push(a,v):import_module('heapq').heappush(a,v)
def heap_pop(a):return import_module('heapq').heappop(a) # 最小値を取り出す

# 二分探索
def bisect_left(a,x):return import_module('bisect').bisect_left(a,x)
def bisect_right(a,x):return import_module('bisect').bisect_left(a,x)
def insert_left(a,x):return import_module('bisect').insert_left(a,bisect_left(a,x))
def insert_right(a,x):return import_module('bisect').insert_right(a,bisect_right(a,x))

# 累積和、累積積、累積GCD
def cumsum(a):return import_module('numpy').cumsum(import_module('numpy').array(a)) # 累積和
def cumprod(a):return import_module('numpy').cumprod(import_module('numpy').array(a)) # 累積積
def cumgcd(a):return import_module('numpy').frompyfunc(gcd_base, 2, 1).accumulate(a, dtype=import_module('numpy').object).astype(import_module('numpy').int) # 累積GCD

class UnionFind(object):
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        x = self.find(x)
        return self.size[x]

def dfs(pos):
    ret = 0
    l = []
    for e in l:
        next = e
        ret += dfs(next)
    return ret

def bfs(l):
    q = init_q(l)
    pos = 0
    q_push(q,pos)
    while q:
        now = q_pop(q)
        for e in l:
            next = e
            q_append(q,next)

# ワーシャルフロイド（グラフの要素数、グラフ）
def warshall_floyd(n,graph):
    d = init_array_2dim(float("inf"),n,n)
    # 初期化
    for i in range(n):
        d[i][i] = 0
        for j in range(n):
            if graph[i][j]:d[i][j] = 1
    # 距離算出
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

# グラフを初期化（グラフの要素数、グラフの線の両端、有向無向）
def init_graph(n,a,directed=False):
    visited = init_array_1dim(False,n)
    graph = init_array_2dim(False,n,n)
    for e in a:
        graph[e[0]-1][e[1]-1] = True
        if not directed:graph[e[1]-1][e[0]-1] = True # 無向グラフの場合
    return visited,graph

def two_pointers(s,threshold,ope='sum'):
    l,r = 0,0
    base = 0 
    if ope == 'sum':base = 0
    if ope == 'prd':base = 1
    diff = 0
    while r < len(s):
        val = 0
        if ope == 'sum':val = base+s[r]
        if ope == 'prd':val = base*s[r]
        if val <= threshold:
            if ope == 'sum':base += s[r]
            if ope == 'prd':base *= s[r]
            diff = max(diff, r-l+1)
            r += 1
        elif l == r:
            r += 1
            l += 1
        else:
            if ope == 'sum':base -= s[l]
            if ope == 'prd':base //= s[l]
            l += 1
    return diff

# ここに実装
def solution():
    global N,H
    N = input_int()
    H = input_ints_list()

    t = 0
    ret = 0
    for h in H:
        if t <= h:
            ret += 1
            t = h
    print(ret)

if __name__ == '__main__':
    solution()
