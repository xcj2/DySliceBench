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
from collections import defaultdict

def main():
	n=II()
	d=defaultdict(int)
	for _ in range(n):
		d[input()]+=1


	print("AC x "+str(d["AC"]))
	print("WA x "+str(d["WA"]))
	print("TLE x "+str(d["TLE"]))
	print("RE x "+str(d["RE"]))






if __name__ == "__main__":
	main()
