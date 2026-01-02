import sys
input = sys.stdin.readline
input = sys.stdin.buffer.readline
def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode('utf-8')
# import numpy as np

import bisect

def main():
	N=II()
	A=LI()
	B=LI()
	C=LI()
	A.sort()
	B.sort()
	C.sort()
	BB=[0]*N
	ans=0
	for i,b in enumerate(B):
		BB[i]=N-bisect.bisect_right(C,b)
	BB.append(0)
	for i in range(N-2,-1,-1):
		BB[i]+=BB[i+1]
	for a in A:
		ans+=BB[bisect.bisect_right(B,a)]
	print(ans)



if __name__ == "__main__":
	main()
