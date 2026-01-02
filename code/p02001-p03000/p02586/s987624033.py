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
	r,c,k=MI()
	G=[[0]*(c+1) for _ in range(r+1)]
	dp=[[[0]*(c+1) for i in range(r+1)] for j in range(4)]
	for _ in range(k):
		rrr,ccc,v=MI()
		G[rrr][ccc]=v
	#print(G)

	#print(dp)

	for rr in range(1,r+1):
		for cc in range(1,c+1):
			if G[rr][cc]==0:
				for i in range(4):
					dp[i][rr][cc]=max(dp[i][rr][cc-1],dp[3][rr-1][cc])
			else:
				dp[0][rr][cc]=max(dp[3][rr-1][cc],dp[0][rr][cc-1])
				dp[1][rr][cc]=max(dp[0][rr][cc]+G[rr][cc],dp[1][rr][cc-1])
				dp[2][rr][cc]=max(dp[1][rr][cc-1]+G[rr][cc],dp[2][rr][cc-1],dp[1][rr][cc])
				dp[3][rr][cc]=max(dp[2][rr][cc-1]+G[rr][cc],dp[3][rr][cc-1],dp[2][rr][cc])
	#print(dp)
	print(dp[-1][-1][-1])















if __name__ == "__main__":
	main()
