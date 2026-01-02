import sys
read = sys.stdin.buffer.read
input = sys.stdin.readline
input = sys.stdin.buffer.readline


#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode('utf-8')

from itertools import permutations

#import numpy as np

def main():
	n,c=MI()
	D=[[0]*(c+1)]
	for _ in range(c):
		D.append([0]+LI())
	#print(D)
	
	C=[[0]*(n+1)]
	for _ in range(n):
		C.append([0]+LI())
	#print(C)
	
	li=[[0]*(c+1) for _ in range(3)]
	for i in range(1,n+1):
		for j in range(1,n+1):
			li[(i+j)%3][C[i][j]]+=1
	#print(li)
	
	ans=10**10
	
	for ii in permutations(range(1,c+1),3):
		ret=0
		#print(ii)
		for a in range(3):
			for b in range(1,c+1):
				#print(li[a][b],D[b][ii[a]])
				ret+=li[a][b]*D[b][ii[a]]
		#print(ans,ret)
		ans=min(ans,ret)
	print(ans)
	
	
	
	
	
	
	

if __name__ == "__main__":
	main()
