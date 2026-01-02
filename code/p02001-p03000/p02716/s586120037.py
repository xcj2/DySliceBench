import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()


def main():
	n=II()
	A=LI()

	X=[-10**10]*(n+1)
	Y=[-10**10]*(n+1)
	X[0]=0
	Y[1]=A[0]
	X[1]=0

	for i in range(2,n+1):
		if i%2==0:
			X[i]=max(Y[i-1],X[i-2]+A[i-1])
		else:
			X[i]=max(X[i-1],X[i-2]+A[i-1])
			Y[i]=Y[i-2]+A[i-1]
	print(X[n])




















if __name__ == "__main__":
	main()
