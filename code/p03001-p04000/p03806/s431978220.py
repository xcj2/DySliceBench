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
	n,ma,mb=MI()
	dp=[[10**6]*(n*10+15) for i in range(n*10+15)]
	for i in range(n+1):
		dp[0][0]=0

	for _ in range(n):
		a,b,c=MI()
		for aa in range(n*10+1,-1,-1):
			for bb in range(n*10+1,-1,-1):
				dp[a+aa][b+bb]=min(dp[aa][bb]+c,dp[a+aa][b+bb])

	ans=10**6

	for i in range(1,1000):
		try:
			ans=min(ans,dp[ma*i][mb*i])
		except:
			break

	print(ans if ans<10**6 else -1)





























if __name__ == "__main__":
	main()
