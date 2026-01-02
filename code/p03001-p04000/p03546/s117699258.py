import sys
input = sys.stdin.readline
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))

# rstrip().decode('utf-8')

#import numpy as np
import heapq

def main():
	h,w=MI()
	
	G=[]
	for _ in range(10):
		c=LI()
		G.append(c)
	#print(G)
	
	for k in range(10):
		for i in range(10):
			for j in range(10):
				G[i][j]=min(G[i][j],G[i][k]+G[k][j])
	
	ans=0
	for _ in range(h):
		row=LI()
		for val in row:
			if abs(val)!=1:
				ans+=G[val][1]
	print(ans)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

if __name__ == "__main__":
	main()
