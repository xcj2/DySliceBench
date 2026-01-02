import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return float(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

from heapq import *

def main():
	n,d,a=MI()
	Q=[]
	heapify(Q)
	for _ in range(n):
		x=LI()
		heappush(Q,x)

	ans=0
	now=0
	li=[[10**10,0]]
	heapify(li)
	while Q:
		#print(Q,li,ans,now)
		if Q[0][0]<li[0][0]:
			x,h=heappop(Q)
			if h-now>0:
				k=(h-now-1)//a+1
				ans+=k
				now+=k*a
				heappush(li,[x+2*d+1,-k*a])
		else:
			x,h=heappop(li)
			now+=h
	print(ans)
















if __name__ == "__main__":
	main()
