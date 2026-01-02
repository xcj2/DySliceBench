from sys import stdin
import math
import bisect
from collections import defaultdict

def IL():return list(map(int, stdin.readline().split()))
def ItoSList(): return list(map(int,list(stdin.readline())))
def IL_reverse():return list(map(int, stdin.readline().split())).reverse()
def Int_all():return list(map(int, stdin))
def sumIL():return sum(list(map(int, stdin.readline().split())))
def SL():return list(map(int, stdin.readline().split()))
def Str_all():return list(map(int, stdin))
def tDL(p,q):return [[0 for i in range(p)] for j in range(q)]


def floyd_warshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])    

N=10
res = float('inf')
dist = [[float("inf")] * N for i in range(N)]
def main():
	H,W = IL()
	for i in range(N):
		dist[i][i] = 0
	
	G = [[] for i in range(N)]
 
	for i in range(10):
	    l = IL()
	    for j in range(10):
	        dist[i][j] = l[j]
	floyd_warshall()

	ans = 0
	memo={}
	for i in range(H):
	    for i in IL():
	        if abs(i) == 1:
	          pass
	        elif i in memo:
	          ans += memo[i]
	        else:
	            t = dist[i][1] 
	            memo[i] = t
	            ans += t
	print(ans)

if __name__ == "__main__": main()
