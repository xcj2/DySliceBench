# 積が負で絶対値が T 以上の組合せ数を求める
# A, B は昇順
def count1(T, A, B):
	if T <= 0 or len(A) == 0 or len(B) == 0:
		return 0

	count, it = 0, -1
	for i in range(len(A) - 1, -1, -1):
		while it + 1 < len(B) and A[i] * B[it + 1] < T:
			it += 1

		# A[i] * B[it], A[i] * B[it + 1], ... は条件を満たす
		count += len(B) - it - 1
	return count


# 積が正で絶対値が T 以下の組合せ数を求める
# 絶対値が T より大きいものの組合せ数を求めてから全体から引く
# A は昇順
def count2(T, A):
	count_all = len(A) * (len(A) - 1) // 2
	count = count1(T + 1, A, A)

	# A[i] * A[i] が余計にカウントされた分を減らす．
	for e in A:
		if e * e >= T + 1:
			count -= 1

	count /= 2 # 同じ配列を渡しているため (i, j) == (j, i) が二回カウントされる

	return count_all - count


if __name__ == "__main__":
	N, K = map(int, input().split())
	A = list(map(int, input().split()))

	# X: 負の数の絶対値の配列
	# Y: 正の数の配列
	# Z: 0 の個数
	X, Y, Z = [], [], 0
	for e in A:
		if e < 0:
			X.append(-e)
		elif e > 0:
			Y.append(e)
		else:
			Z += 1
	X.sort()
	Y.sort()


	# 積が T 以下な組合せ数が K 未満か？
	def check(T):
		count = 0
		if T < 0:
			count += count1(abs(T), X, Y)
		else:
			count += len(X) * len(Y) # 結果が負
			count += Z * (Z - 1) // 2 + Z * (N - Z) # 結果が 0
			count += count2(T, X) + count2(T, Y)

		return count < K


	ok, ng = -10 ** 18, 10 ** 18
	while ng - ok > 1:
		mid = (ok + ng) // 2
		
		if check(mid):
			ok = mid
		else:
			ng = mid

	print(ok + 1)
