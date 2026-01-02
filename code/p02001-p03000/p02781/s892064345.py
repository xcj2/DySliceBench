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
	n=RD()
	k=II()

	dp=[[[0]*2 for _ in range(k+2)] for _ in range(len(n)+1)]
	#print(dp)

	dp[0][0][0]=1

	for i in range(len(n)):
		now=int(n[i])
		for j in range(k+1):
			#print(i,j,now)
			dp[i+1][j+(now!=0)][0]+=dp[i][j][0]
			dp[i+1][j][1]+=dp[i][j][1]+dp[i][j][0]*(now!=0)
			dp[i+1][j+1][1]+=dp[i][j][1]*9+dp[i][j][0]*(now-1 if now>0 else 0)
		#print(dp)
	print(dp[len(n)][k][0]+dp[len(n)][k][1])

















if __name__ == "__main__":
	main()
