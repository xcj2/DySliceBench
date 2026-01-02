import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return float(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()



def main():
	n=II()
	A=[II() for _ in range(n)]+[0]


	if A[0]!=0:
		print(-1)
		exit()

	ans=0

	for i,j in zip(A[:-1],A[1:]):
		if j-i>=2:
			print(-1)
			exit()
		elif j-i<=0:
			ans+=i

	print(ans)












if __name__ == "__main__":
	main()
