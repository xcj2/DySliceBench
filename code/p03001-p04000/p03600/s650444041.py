import sys
read = sys.stdin.buffer.read
input = sys.stdin.readline
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode('utf-8')

import copy

def main():
	n=II()
	A=[]
	for _ in range(n):
		a=LI()
		A.append(a)

	for i in range(n):
		A[i][i]=10**10

	B=copy.deepcopy(A)

	for k in range(n):
		for i in range(n):
			for j in range(n):
				if i!=j:
					B[i][j]=min(B[i][j],B[i][k]+B[k][j])

	if A!=B:
		print(-1)
		exit(0)

	for k in range(n):
		for i in range(n):
			for j in range(n):
				if B[i][j]==B[i][k]+B[k][j]:
					A[i][j]=0

	ans=0

	for i in range(n):
		for j in range(i,n):
			if i!=j:
				ans+=A[i][j]

	print(ans)


if __name__ == "__main__":
	main()