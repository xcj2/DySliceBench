import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict
import bisect

con = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

def Binary_Search(A, N, M):
	#初期化
	left = 0
	right = 10 ** 7
	ans = 0
	#累積和
	Asum = [0]
	for i in range(N):
		Asum.append(Asum[i] + A[-1 - i])

	leftj = [INF, INF]
	rightj = [0, 0]
	#二分探索
	while left <= right:
		mid = (left + right) // 2
		var = 0
		happiness = 0
		for i in range(N):
			ind = bisect.bisect_left(A, mid - A[i])
			ind = N - ind
			var += ind
			happiness += ind * A[i] + Asum[ind]

		# print(var, happiness)
		if var == M:
			return happiness
		elif var > M:
			leftj = min(leftj, [var, -mid])
			left = mid + 1
		else:
			ans = max(ans, happiness)
			rightj = max(rightj, [var, -mid])
			right = mid - 1

	# print(ans)
	# print(leftj)
	# print(rightj)

	ans = ans + (M - rightj[0]) * (-leftj[1])
			
	return ans


#処理内容
def main():
	N, M = getlist()
	A = getlist()
	A.sort()
	ans = Binary_Search(A, N, M)

	print(ans)

if __name__ == '__main__':
	main()