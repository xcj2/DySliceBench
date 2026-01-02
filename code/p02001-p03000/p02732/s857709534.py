import sys
input = sys.stdin.readline
#input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode('utf-8')
#import numpy as np

from collections import deque

def main():
	n=II()
	A=LI()
	B=[0]*(n+1)
	for i in A:
		B[i]+=1

	ans=0
	for i in B:
		ans+=i*(i-1)//2
	#print(ans)
	for i in A:
		print(ans-B[i]+1)









if __name__ == "__main__":
	main()