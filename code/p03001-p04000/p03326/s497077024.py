import sys
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
# rstrip().decode()

#import numpy as np
#import bisect

from itertools import product

def main():
	n,m=MI()
	li=[[] for _ in range(8)]

	for _ in range(n):
		a,b,c=MI()
		for i,e in enumerate(product((1,-1),repeat=3)):
			li[i].append(a*e[0]+b*e[1]+c*e[2])

	ans=0

	for l in li:
		l.sort(reverse=True)
		ans=max(ans,sum(l[:m]))
	print(ans)



if __name__ == "__main__":
	main()
