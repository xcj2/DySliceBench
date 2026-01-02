import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

from collections import deque

def main():
	h,w,m=MI()
	A=[0]*(h+1)
	B=[0]*(w+1)
	C=[[] for _ in range(h+1)]

	for _ in range(m):
		hh,ww=MI()
		A[hh]+=1
		B[ww]+=1
		C[hh].append(ww)


	for i in range(h+1):
		C[i].sort()

	AA=max(A)
	BB=max(B)

	x=[]
	y=[]

	for i,v in enumerate(A):
		if v==AA:
			x.append(i)

	for i,v in enumerate(B):
		if v==BB:
			y.append(i)

	#print(x,y,AA,BB)
	#print(C)
	ans=0

	for i in x:
		C[i].append(10**7)
		#print("a")
		#print(C[i])
		#print(y)
		a=0
		for j in y:
			while a<len(C[i]):
				if j==C[i][a]:
					a+=1
					break
				elif j<C[i][a]:
					print(AA+BB)
					exit()
				else:
					a+=1

	print(AA+BB-1)
















if __name__ == "__main__":
	main()
