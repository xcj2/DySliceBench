import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
enum = enumerate
inf = 1001001002002002002

import random

def linput(ty=int, cvt=list):
	return cvt(map(ty,input().rstrip().split()))

def vinput(rep=1, ty=int, cvt=list):
	return cvt(ty(input().rstrip()) for _ in "*"*rep)

def gcd(a: int, b: int):
	while b: a, b = b, a%b
	return a

def lcm(a: int, b: int):
	return a * b // gcd(a, b)

def bye(res):
	sT = "No Yes".split()
	print(sT[res])
	#exit(0)

def sol(N,vF):
	P,E = 1e9, 1e-3
	vA = [int(f*P+E) for f in vF]
	
	def divcnt(n):
		m,n = n,n
		a,b = 0,0
		while m%2<1: m//=2; a+=1
		while n%5<1: n//=5; b+=1
		return a,b

	vM = [divcnt(a) for a in vA]
	
	mX = [[0,]*50 for _ in "*"*50]
	for a,b in vM:
		mX[b][a] += 1
	
	mC = [[0,]*51,]
	for vX in mX:
		vC = [0,]
		t = 0
		for c,x in zip(mC[-1][1:],vX):
			t += x
			vC.append(t+c)
		mC.append(vC)
	
	#print(*mC[:20], sep="\n")###
	
	res = 0
	
	for a,b in vM:
		x = max(18-a, 0)
		y = max(18-b, 0)
		t = N - mC[y][-1] - mC[-1][x] + mC[y][x]
		if t and x<=a and y<=b:
			t-=1
		#t//=2
		#print(t,N,mC[y][-1],mC[-1][x],mC[y][x],a,b,x,y)##
		res += t

	print(res//2)


def main():
	N, = linput()
	sol(N, vinput(N,float))

if __name__ == "__main__":
	main()
