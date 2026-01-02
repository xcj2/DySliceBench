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

from collections import deque

def main():
	n,c=MI()

	li=[[0]*c for _ in range(10**5+1)]
	#print(li)

	for _ in range(n):
		s,t,cc=MI()
		for i in range(s-1,t):
			li[i][cc-1]=1

	ans=0

	for A in li:
		ans=max(ans,sum(A))
	print(ans)









if __name__ == "__main__":
	main()
