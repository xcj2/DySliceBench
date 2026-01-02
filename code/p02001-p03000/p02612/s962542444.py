import sys
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
# rstrip().decode()

#import numpy as np

def main():
	n=II()
	if n%1000==0:
		print(0)
	else:
		print((n//1000)*1000+1000-n)


if __name__ == "__main__":
	main()
