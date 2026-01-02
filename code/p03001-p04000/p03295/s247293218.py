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


#import numpy as np

def main():
	n,m=MI()
	li=[LI() for _ in range(m)]
	#print(li)
	li.sort(key=lambda x:x[1])
	#print(li)
	
	now=0
	ans=0
	
	for a,b in li:
		if now<=a:
			ans+=1
			now=b
	
	print(ans)
	
	

if __name__ == "__main__":
	main()
