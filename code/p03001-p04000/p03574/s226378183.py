from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
AtoZ = [chr(i) for i in range(65,65+26)]
atoz = [chr(i) for i in range(97,97+26)]

def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())


H,W = inpl()
map = []
map.append(['.']*(W+2))
for y in range(H):
	map.append(['.'] + list(input()) + ['.'])
map.append(['.']*(W+2))

ans = [[0 for i in range(W)] for j in range(H)]

def check(x,y):
	global map
	tmp  = 0
	for yy in range(y-1,y+2):
		for xx in range(x-1,x+2):
			if map[yy][xx] == '#':
				tmp += 1
	return str(tmp)

for y in range(1,H+1):
	for x in range(1,W+1):
		if map[y][x] == '#':
			ans[y-1][x-1] = '#'
		else:
			ans[y-1][x-1] = check(x,y)

for an in ans:
	print(''.join(an))
