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

#2234
#import numpy as np

def main():
	m=II()
	di=0
	su=0
	for _ in range(m):
		d,c=MI()
		di+=c
		su+=d*c

	print((su-1)//9+di-1)

if __name__ == "__main__":
	main()