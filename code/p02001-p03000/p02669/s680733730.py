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

def sol2(N,A,B,C,D):
	dM = dict({0: 0, 1: D})
	
	def dfs(n):
		if n in dM:
			return dM[n]

		res = min(
				D*n,
				D*(n%2) + A + dfs(n//2),
				D*(n%3) + B + dfs(n//3),
				D*(n%5) + C + dfs(n//5),
				D*(n%2) + A + dfs((n+1)//2),
				D*((3 - n%3)%3) + B + dfs((n+2)//3),
				D*((5 - n%5)%5) + C + dfs((n+4)//5)
			)

		dM[n] = res
		return res
	
	dfs(N)
	#print(dM)###
	print(dM[N])


def main():
	T, = linput()
	for _ in "*"*T:
		sol2(*linput())

def ran():
	vRan = [random.randint(1,10) for _ in "*"*5]
	print(vRan)
	sol2(*vRan)

if __name__ == "__main__":
	main()
	#ran()
