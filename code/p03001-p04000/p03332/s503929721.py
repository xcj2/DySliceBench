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
	n,a,b,k=MI()

	m=998244353

	C=[1]
	for i in range(n):
		t=C[-1]*(n-i)*pow(i+1,m-2,m)
		C.append(t%m)
	#print(C)

	ans=0

	for x in range(n+1):
		if (k-a*x)%b==0:
			y=(k-a*x)//b
			if 0<=y<=n:
				ans+=C[x]*C[y]
				ans%=m
	print(ans)

























if __name__ == "__main__":
	main()
