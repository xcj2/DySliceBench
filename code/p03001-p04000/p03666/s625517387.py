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

#import numpy as np

def main():
	n,a,b,c,d=MI()

	n-=1
	x=abs(b-a)

	ans="NO"

	for i in range(n):
		r=(n-i)*d-c*i
		l=(n-i)*c-d*i
		#print(l,x,r)
		if l<=x<=r:
			ans="YES"
			#print(l,x,r)
			break
		elif l<0:
			break

	print(ans)





if __name__ == "__main__":
	main()
