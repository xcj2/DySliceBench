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

def main():
	n,m=MI()
	A=[0]+LI()

	for i in range(n):
		A[i+1]+=A[i]
		A[i+1]%=m
	#print(A)

	d=defaultdict(int)

	for i in A:
		d[i]+=1
	#print(d)

	ans=0
	for k,v in d.items():
		ans+=v*(v-1)//2
	print(ans)











if __name__ == "__main__":
	main()
