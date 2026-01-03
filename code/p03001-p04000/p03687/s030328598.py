import sys
input = sys.stdin.readline
enum = enumerate

import collections
import random

def linput(ty=int, cvt=list):
	return cvt(map(ty,input().split()))

def gcd(a: int, b: int):
	while b: a, b = b, a%b
	return a

def lcm(a: int, b: int):
	return a * b // gcd(a, b)

def dist(x1,y1,x2,y2):
	return abs(x1-x2)+abs(y1-y2)

def main():
	S = input().rstrip()
	#vS = [input().rstrip() for _ in [0,]*N]
	N = len(S)
	oA = ord("a")
	vD = [chr(i+oA) for i in range(26)]
	#vD += [".","#"]

	res = 0
	M = N
	
	# dp[i..M][d..26] = y/n
	vN = [[0,]*26 for _ in "*"*M]

	for i,s in enum(S):
		d = ord(s)-oA
		vN[i][d] = 1

	while M:
		ok = 0
		for d in range(26):
			for i in range(M):
				if not vN[i][d]: break
			else:
				ok = 1; break
		if ok: break
		M -= 1
		for d in range(26):
			for i in range(M):
				vN[i][d] |= vN[i+1][d]
	
	res = N - M
	print(res)
	#sT = "No Yes".split()
	#print(sT[res])
	

if __name__ == "__main__":
	main()
