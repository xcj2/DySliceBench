#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict
import itertools

#Binary Indexed Tree
#O(logN)でtに1点加算、t以下の合計を得る

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

#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	#入力処理
	N = int(input())
	A = getlist()
	B = getlist()
	omote = []
	ura = []
	for i in range(N):
		if i % 2 == 0:
			omote.append([A[i], i])
			ura.append([B[i], i])
		else:
			omote.append([B[i], i])
			ura.append([A[i], i])

	#半分全列挙
	seq = [i for i in range(N)]
	alllist = list(itertools.combinations(seq, int((N + 1) // 2)))
	M = len(alllist)
	#print(alllist)
	ans = float("inf")
	for i in range(M):
		lis = alllist[i]
		USE = [0] * N
		for j in lis:
			USE[j] = 1 #1:表 0:裏
		X = []
		Y = []
		for j in range(N):
			if USE[j] == 1:
				X.append(omote[j])
			else:
				Y.append(ura[j])
		X = sorted(X)
		Y = sorted(Y)
		sequence = []
		for j in range(N):
			if j % 2 == 0:
				sequence.append(X[int(j // 2)])
			else:
				sequence.append(Y[int(j // 2)])
		#print(sequence)
		judge = "Yes"
		for j in range(N - 1):
			if sequence[j][0] > sequence[j + 1][0]:
				judge = "No"
				break
		if judge == "Yes":
			bit = []
			for j in range(N):
				bit.append(sequence[j][1] + 1)
			# print(bit)
			val = 0
			calc = BIT(50)
			for j in range(N):
				calc.add(bit[j], 1)
				val += j + 1 - calc.sum(bit[j])
			# print(val)
			ans = min(ans, val)

	if ans == float("inf"):
		print(-1)
	else:
		print(ans)


# N = int(input())
# M = int(input())
# A = getlist()

# bit = BIT(M)
# for i in range(N):
# 	bit.add(A[i], 1)
# 	ans += i + 1 - bit.sum(A[i])

# print(ans)


if __name__ == '__main__':
	main()