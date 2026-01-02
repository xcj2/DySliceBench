import importlib
import_module = lambda name:importlib.import_module(name)

input = import_module('sys').stdin.readline
input_int = lambda:int(input())
input_ints = lambda:map(int,input().split())
input_ints_list = lambda:list(input_ints())
input_str = lambda:input()
input_strs = lambda:input().split()
input_lines = lambda n,f:[f() for _ in range(n)]

gcd_base = lambda a,b:import_module('fractions').gcd(a,b) # 最大公約数（2値)
gcd = lambda a:import_module('functools').reduce(gcd_base,a) # 最大公約数（リスト）
lcm_base = lambda a,b:(a*b)//import_module('fractions').gcd(a,b) # 最小公倍数(2値)
lcm = lambda a:import_module('functools').reduce(lcm_base,a,1) # 最小公倍数(リスト)

permutations = lambda a,n:import_module('itertools').permutations(a,n) # 順列
combinations = lambda a,n:import_module('itertools').combinations(a,n) # 組み合わせ
product = lambda a,b:import_module('itertools').product(a,b) # 二つのリストの直積

init_array_1dim = lambda v,n:[v]*n
init_array_2dim = lambda v,n,m:[init_array_1dim for _ in range(m)]

# 四捨五入はround
ceil = lambda a:import_module('math').ceil(a) # 切り上げ
floor = lambda a:import_module('math').floor(a) # 切り捨て

# キュー
convert_list_to_queue = lambda a:import_module('collections').deque(a)
pop_q = lambda a:a.popleft()
push_q = lambda a,e:a.appendleft(e)
push_q_list = lambda a,l:a.extendleft(l) 

# プライオリティキュー
def init_head(a):import_module('heapq').heapify(a)
def heap_push(a,v):import_module('heapq').heappush(a,v)
heap_pop = lambda a:import_module('heapq').heappop(a) # 最小値を取り出す

# 二分探索
bisect_left = lambda a,x:import_module('bisect').bisect_left(a,x)
bisect_right = lambda a,x:import_module('bisect').bisect_left(a,x)
insert_left = lambda a,x:import_module('bisect').insert_left(a,bisect_left(a,x))
insert_right = lambda a,x:import_module('bisect').insert_right(a,bisect_right(a,x))

# 累積和、累積積、累積GCD
cumsum = lambda a:import_module('numpy').cumsum(import_module('numpy').array(a)) # 累積和
cumprod = lambda a:import_module('numpy').cumprod(import_module('numpy').array(a)) # 累積積
cumgcd = lambda a:import_module('numpy').frompyfunc(gcd, 2, 1).accumulate(a, dtype=import_module('numpy').object).astype(import_module('numpy').int) # 累積GCD

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

# グラフで全部到達できる経路が何個あるか
def dfs_graph(v,n,graph,visited):
    if all(visited):return 1 # 全部到達できたら1を返す
    ans = 0
    for i in range(n):
        if not graph[v][i]:continue # 結ぶ線がないときはスキップ
        if visited[i]:continue # 到達済みだったらスキップ
        visited[i] = True
        ans += dfs_graph(i,n,graph,visited)
        visited[i] = False
    return ans

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

def solution():
    # ここに実装
    global N,V,C
    N = input_int()
    V = input_ints_list()
    C = input_ints_list()

    vals = [x-y for x,y in zip(V,C) if x-y > 0]
    print(sum(vals))
        
	
if __name__ == '__main__':
    solution()
