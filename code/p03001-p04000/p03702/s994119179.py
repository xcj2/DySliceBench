#設定
import sys
input = sys.stdin.buffer.readline

INF = float("inf")

def getlist():
	return list(map(int, input().split()))

def Binary_Search(H, N, A, B):
	#初期化
	left = 0
	right = 2 * (10 ** 9)
	ans = INF
	ex = A - B
	
	#二分探索
	while left <= right:
		mid = (left + right) // 2
		cnt = 0
		for i in range(N):
			if H[i] - mid * B > 0:
				if (H[i] - mid * B) % ex == 0:
					cnt += int((H[i] - mid * B) // ex)
				else:
					cnt += int((H[i] - mid * B) // ex) + 1
		#print(mid, cnt)
		if mid >= cnt:
			ans = min(ans, mid)
			right = mid - 1
		else:
			left = mid + 1

	return ans

#処理内容
def main():
	N, A, B = getlist()
	H = []
	for i in range(N):
		H.append(int(input()))
	
	ans = Binary_Search(H, N, A, B)
	print(ans)

if __name__ == '__main__':
	main()