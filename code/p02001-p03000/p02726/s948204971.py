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

#
#import numpy as np

def main():
	n,x,y=MI()
	ans=[0]*(n)

	for i in range(1,n):
		for j in range(i+1,n+1):
			dis=min(j-i,abs(x-i)+abs(y-j)+1,abs(x-j)+abs(y-i)+1)
			ans[dis]+=1


	print(*ans[1:],sep="\n")


















if __name__ == "__main__":
	main()