import sys
read = sys.stdin.buffer.read
#input = sys.stdin.readline
#input = sys.stdin.buffer.readline

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
import math


def main():
	
	k=II()
	
	ans=0
	
	li=[[0]*(k+1) for i in range(k+1)]
	
	for a in range(1,k+1):
		for b in range(1,k+1):
			for c in range(1,k+1):
				d=math.gcd(a,b)
				ans+=math.gcd(d,c)
				
	
	print(ans)





	
if __name__ == "__main__":
	main()
