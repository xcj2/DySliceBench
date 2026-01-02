#ライブラリインポート
from collections import defaultdict
INF = float("inf")
#入力受け取り
def getlist():
	return list(map(int, input().split()))

#更新クエリ
def update(data, k, x, N0):
	k += N0 - 1
	data[k] = x
	while k > 0:
		k = (k - 1) // 2
		data[k] = data[2 * k + 1] | data[2 * k + 2]

#求値クエリ 最初:query(a, b, 0, 0, N0)
def query(data, a, b, k, l, r):
	if r <= a or b <= l:
		return 0
	if a <= l and r <= b:
		return data[k]
	else:
		vl = query(data, a, b, k * 2 + 1, l, (l + r) // 2)
		vr = query(data, a, b, k * 2 + 2, (l + r) // 2, r)
		return vl | vr

#処理内容
def main():
	N = int(input())

	#セグ木初期化
	N0 = 2 ** (N - 1).bit_length()
	S = list(input())
	data = [0] * (2 * N0 - 1)
	for i in range(N):
		data[N0 - 1 + i] = 2 ** (ord(S[i]) - 97)
		ind = N0 - 1 + i
		while ind > 0:
			ind = (ind - 1) // 2
			data[ind] = data[ind * 2 + 1] | data[ind * 2 + 2]

	Q = int(input())
	for _ in range(Q):
		que = list(input().split())
		if que[0] == "1":
			i = int(que[1]) - 1
			c = 2 ** (ord(que[2]) - 97)
			update(data, i, c, N0)
		else:
			a = int(que[1])
			b = int(que[2])
			a -= 1
			jjj = query(data, a, b, 0, 0, N0)
			ans = 0
			while jjj != 0:
				if jjj % 2 == 1:
					ans += 1
				jjj = int(jjj // 2)

			print(ans)


if __name__ == '__main__':
	main()