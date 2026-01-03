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

def dfs_graph(v,n,graph,visited):
	if all(visited):return 1
	ans = 0
	for i in range(n):
		if graph[v][i] == False:continue
		if visited[i]:continue
		visited[i] = True
		ans += dfs_graph(i,n,graph,visited)
		visited[i] = False
	return ans

def init_graph(n,a,directed=False):
    visited = init_array_1dim(False,n)
    graph = init_array_2dim(False,n,n)
    for e in a:
        graph[e[0]-1][e[1]-1] = True
        if not directed:graph[e[1]-1][e[0]-1] = True # 無向グラフの場合
    return visited,graph

def solution():
    N,M = input_ints()
    ab = input_lines(M,input_ints_list)
    visited,graph = init_graph(N,ab)
    visited[0] = True
    print(dfs_graph(0,N,graph,visited))

if __name__ == '__main__':
    solution()