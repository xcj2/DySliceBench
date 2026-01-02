import sys
# import numpy as np

def I():
	return int(sys.stdin.readline().rstrip())

def LI():
	return list(map(int, sys.stdin.readline().rstrip().split()))

def main():
	N = I()
	activity = []
	for i in range(N):
		activity.append(LI())
	
	# dp = np.zeros((N, 3), dtype=int)
	dp = [[0, 0, 0] for _ in range(N)]
	dp[0][0] = activity[0][0]
	dp[0][1] = activity[0][1]
	dp[0][2] = activity[0][2]
	for i in range(1, N):
		dp[i][0] = max(dp[i-1][1] + activity[i][0], dp[i-1][2] + activity[i][0])
		dp[i][1] = max(dp[i-1][0] + activity[i][1], dp[i-1][2] + activity[i][1])
		dp[i][2] = max(dp[i-1][0] + activity[i][2], dp[i-1][1] + activity[i][2])
	print(max(dp[-1]))

if __name__ == "__main__":
	main()