#設定
import sys
input = sys.stdin.buffer.readline

INF = float("inf")

def getlist():
	return list(map(int, input().split()))

#二分探索基本形 L:リスト x:値 n:リスト長
def Binary_Search(A, F, N, K):
	#初期化
	left = 0
	right = 10 ** 12
	ans = INF
	
	#二分探索
	while left <= right:
		mid = (left + right) // 2
		cnt = 0
		for i in range(N):
			if A[i] * F[i] > mid:
				cnt += (A[i] - int(mid // F[i]))
		if cnt <= K:
			right = mid - 1
			ans = min(ans, mid)
		else:
			left = mid + 1

	return ans

#処理内容
def main():
	N, K = getlist()
	A = getlist()
	F = getlist()
	A = sorted(A)
	F = sorted(F)[::-1]
	ans = Binary_Search(A, F, N, K)
	print(ans)

if __name__ == '__main__':
	main()