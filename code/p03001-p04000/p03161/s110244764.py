import sys
# import numpy as np
inp = sys.stdin.readline
read = lambda: list(map(int, inp().strip().split()))
# import profile

def solve():
    n, k =read(); arr = read()
    dp = [-1]*n; dp[0] = 0
    for i in range(n):
    	for j in range(1, k+1):
    		if i-j >-1:
    			tem = dp[i-j]+abs(arr[i-j] - arr[i])
    			if dp[i] == -1:
    				dp[i] = tem
    			elif dp[i] > tem:
    				dp[i] = tem
    				# dp[i] = min(dp[i], tem)
    print(dp[-1])

def one():
	l = [0]*10**7
def two():
	l = [0 for i in range(10**7)]

if __name__ == "__main__":
	solve()
	# cProfile.run(solve())
	# profile.run(one())
	# cProfile.run()