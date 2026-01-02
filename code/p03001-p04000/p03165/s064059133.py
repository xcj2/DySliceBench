import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
printV = lambda x: print(*x, sep="\n")
printH = lambda x: print(" ".join(map(str,x)))
def IS(): return sys.stdin.readline()[:-1]
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LII(rows_number): return [II() for _ in range(rows_number)]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]

def main():
	s = IS()
	t = IS()
	n = len(s)
	m = len(t)
	dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
	for i in range(n):
		for j in range(m):
			if(s[i]==t[j]):
				dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1],dp[i][j]+1)
			else:
				dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

	ans = ''
	while (n>0  and m>0):
	    if dp[n][m] == dp[n-1][m]:
	        n -= 1
	    elif dp[n][m] == dp[n][m-1]:
	        m -= 1
	    else:
	        ans += s[n-1]
	        n -= 1
	        m -= 1
	print(ans[::-1])

if __name__ == '__main__':
	main()