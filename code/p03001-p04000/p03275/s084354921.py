import sys; input = sys.stdin.buffer.readline
from collections import defaultdict
con = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

class BIT:
	def __init__(self, N):
		self.size = N
		self.tree = [0] * (N + 1)

	def sum(self, t):
		s = 0
		while t > 0:
			s += self.tree[t]
			t -= t & -t
		return s

	def add(self, t, x):
		while t <= self.size:
			self.tree[t] += x
			t += t & -t

def Binary_Search(A, B, N):
	#初期化
	left = 0
	right = N - 1
	ans = 0
	
	#二分探索
	while left <= right:
		mid = (left + right) // 2
		var = B[mid]
		newlist = [None] * N
		#境界判定して1,-1で構成されるリストの構築
		for i in range(N):
			if A[i] >= var:
				newlist[i] = 1
			else:
				newlist[i] = -1
		#累積和
		newlistsum = [0]
		for i in range(N):
			newlistsum.append(newlistsum[-1] + newlist[i])
		cnt = 0
		bit = BIT(2 * N + 1)
		for i in range(N + 1):
			bit.add(newlistsum[i] + N, 1)
			cnt += bit.sum(newlistsum[i] + N) - 1

		if 4 * cnt >= N * (N + 1):
			ans = max(ans, B[mid])
			left = mid + 1
		else:
			right = mid - 1

	return ans

#処理内容
def main():
	N = int(input())
	A = getlist()
	B = sorted(A)
	ans = Binary_Search(A, B, N)
	print(ans)

if __name__ == '__main__':
	main()