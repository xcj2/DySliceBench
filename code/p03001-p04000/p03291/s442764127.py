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
	s=RD()
	n=len(s)

	dp=[[0]*4 for _ in range(n+1)]
	dp[0][0]=1


	for i,ss in enumerate(s):
		if s[i]=="A":
			dp[i+1][0]=dp[i][0]
			dp[i+1][1]=dp[i][0]+dp[i][1]
			dp[i+1][2]=dp[i][2]
			dp[i+1][3]=dp[i][3]
		elif s[i]=="B":
			dp[i+1][0]=dp[i][0]
			dp[i+1][1]=dp[i][1]
			dp[i+1][2]=dp[i][1]+dp[i][2]
			dp[i+1][3]=dp[i][3]
		elif s[i]=="C":
			dp[i+1][0]=dp[i][0]
			dp[i+1][1]=dp[i][1]
			dp[i+1][2]=dp[i][2]
			dp[i+1][3]=dp[i][2]+dp[i][3]
		else:
			dp[i+1][0]=dp[i][0]*3
			dp[i+1][1]=dp[i][0]+dp[i][1]*3
			dp[i+1][2]=dp[i][1]+dp[i][2]*3
			dp[i+1][3]=dp[i][2]+dp[i][3]*3

		for j in range(4):
			dp[i+1][j]%=10**9+7


	print(dp[-1][-1])











if __name__ == "__main__":
	main()
