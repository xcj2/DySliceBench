#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict

con = 10 ** 9 + 7
#入力受け取り
def getlist():
	return list(map(int, input().split()))

def Binary_Search(A, N, M, V, P):
	#初期化
	#B:累積和
	B = [0]
	for i in range(N):
		B.append(B[i] + A[i])
	ans = float("inf")
	left = 0
	right = N - 1
	#二分探索
	while left <= right:
		mid = (left + right) // 2
		if (A[mid] + M) * (N - P - mid) >= B[N - P + 1] - B[mid + 1] + (V - mid - P) * M and A[mid] + M >= A[N - P]:
			ans = min(ans, mid)
			right = mid - 1
		elif mid >= N - P:
			ans = min(ans, mid)
			right = mid - 1
		else:
			left = mid + 1

	return N - ans

#処理内容
def main():
	N, M, V, P = getlist()
	A = sorted(getlist())
	ans = Binary_Search(A, N, M, V, P)

	print(ans)

if __name__ == '__main__':
	main()