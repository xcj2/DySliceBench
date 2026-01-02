import sys
#input = sys.stdin.buffer.readline


#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

#import numpy as np

def main():
	h,w,k=MI()
	G=[]
	for _ in range(h):
		G.append(list(input()))
	#print(G)
	ans=0

	for i in range(1<<h):
		for j in range(1<<w):
			cnt=0
			for ii in range(h):
				for jj in range(w):
					#print(i,j,ii,jj,)
					if i&1<<ii and j&1<<jj and G[ii-1][jj-1]=="#":
						#print(1<<i)
						cnt+=1
			if cnt==k:
				ans+=1
	print(ans)







if __name__ == "__main__":
	main()
