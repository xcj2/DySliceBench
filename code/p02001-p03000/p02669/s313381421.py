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

from collections import defaultdict
from heapq import *

def main():
	t=II()
	while t:
		t-=1
		n,a,b,c,d=MI()
		Q=[-n,0]
		heapify(Q)
		D=defaultdict(lambda:10**18)
		D[n]=0
		k=n+1
		while Q:
			now=-heappop(Q)
			#print(now,"a")
			if now==0:
				print(D[0])
				break

			if now<k:
				q2,r2=divmod(now,2)
				q3,r3=divmod(now,3)
				q5,r5=divmod(now,5)

				#print(now)
				if D[q5]>D[now]+c+r5*d:
					D[q5]=D[now]+c+r5*d
					heappush(Q,-q5)
				if r5!=0 and D[q5+1]>D[now]+c+(5-r5)*d:
					D[q5+1]=D[now]+c+(5-r5)*d
					heappush(Q,-q5-1)

				if D[q3]>D[now]+b+r3*d:
					D[q3]=D[now]+b+r3*d
					heappush(Q,-q3)
				if r3!=0 and D[q3+1]>D[now]+b+(3-r3)*d:
					D[q3+1]=D[now]+b+(3-r3)*d
					heappush(Q,-q3-1)

				if D[q2]>D[now]+a+r2*d:
					D[q2]=D[now]+a+r2*d
					heappush(Q,-q2)
				if r2!=0 and D[q2+1]>D[now]+a+(2-r2)*d:
					D[q2+1]=D[now]+a+(2-r2)*d
					heappush(Q,-q2-1)

				D[0]=min(D[0],D[now]+now*d)







if __name__ == "__main__":
	main()
