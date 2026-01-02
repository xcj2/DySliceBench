import sys
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
# rstrip().decode()

import heapq

def main():
	t=II()
	for _ in range(t):
		n=II()
		L=[]
		R=[]
		ans=0
		for _ in range(n):
			k,l,r=MI()
			if l>=r:
				ans+=r
				L.append((k,l-r))
			else:
				ans+=l
				R.append((n-k,r-l))
		L.sort()
		R.sort()
		#print(L,R,ans)

		Q=[]
		heapq.heapify(Q)

		for k,v in L:
			ans+=v
			heapq.heappush(Q,v)
			if len(Q)>k:
				#print(Q,k,ans)
				vv=heapq.heappop(Q)
				ans-=vv

		Q=[]
		heapq.heapify(Q)

		for k,v in R:
			ans+=v
			heapq.heappush(Q,v)
			if len(Q)>k:
				#print(Q,k,ans)
				vv=heapq.heappop(Q)
				ans-=vv
		print(ans)






if __name__ == "__main__":
	main()
