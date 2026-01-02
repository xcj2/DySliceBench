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
from itertools import combinations

def main():
	n=II()
	d=LI()
	d.sort()
	t=[0]*25
	t[0]=1
	t[24]=1

	for i in range(n):
		if i%2==0:
			t[d[i]]+=1
		else:
			t[24-d[i]]+=1

	if max(t)>=2:
		print(0)
		exit(0)

	ans=12
	cnt=0
	for i in range(1,25):
		if t[i]==0:
			cnt+=1
		else:
			ans=min(ans,cnt+1)
			cnt=0

	print(ans)


if __name__ == "__main__":
	main()
