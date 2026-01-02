import sys

input_int = lambda:int(input())
input_ints = lambda:map(int,input().split())
input_ints_list = lambda:list(input_ints())
input_str = lambda:input()
input_strs = lambda:input().split()
input_lines = lambda n,f:[f() for _ in range(n)]

import functools,fractions
gcd = lambda a:functools.reduce(fractions.gcd,a) # 最大公約数（リスト）
lcm_base = lambda a,b:(a*b)//fractions.gcd(a,b) # 最小公倍数(2値)
lcm = lambda a:functools.reduce(lcm_base,a,1) # 最小公倍数(リスト)

import itertools
permutations = lambda a,n:itertools.permutations(a,n) # 順列
combinations = lambda a,n:itertools.combinations(a,n) # 組み合わせ
product = lambda a,b:itertools.product(a,b) # 二つのリストの直積

init_array_1dim = lambda v,n:[v for _ in range(n)]
init_array_2dim = lambda v,n,m:[[v for _ in range(n)] for _ in range(m)]

import math
# 四捨五入はround
ceil = lambda a:math.ceil(a) # 切り上げ
floor = lambda a:math.floor(a) # 切り捨て

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

def solution():
	# ここに実装
    N,M = input_ints()
    AB = input_lines(M,input_ints_list)

    ans = []
    count = N*(N-1)//2 # 線一つもない時は2つ選んだ組み合わせ数
    uf = UnionFind(N)
    # 線を後ろから追加していく感じで処理を進める
    while(AB):
        ans.append(count)
        a,b = AB.pop()
        if not uf.is_same(a-1,b-1):
            count -= uf.get_size(a-1)*uf.get_size(b-1)
            uf.union(a-1,b-1)
    
    ans.reverse()
    for _ans in ans:
        print(_ans)
	
if __name__ == '__main__':
    solution()