import sys

input=sys.stdin.buffer.readline


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

from collections import defaultdict

def main():
	n=II()
	A=LI()
	
	X=defaultdict(int)
	Y=defaultdict(int)
	
	for i,v in enumerate(A):
		X[i+v]+=1
		Y[i-v]+=1
	
	ans=0
	for k,v in X.items():
		ans+=v*Y[k]
	print(ans)
	
	







if __name__=="__main__":
	main()
