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

from itertools import combinations

def main():
	k,n=MI()
	A=LI()
	ans=A[-1]-A[0]

	for i in range(n-1):
		ans=min(ans,A[i]+k-A[i+1])

	print(ans)





if __name__ == "__main__":
	main()