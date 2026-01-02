
# EDPC Q - Flowers
# 重み付きのLISと言って良いような問題
# これは、LISのdpを少し改造すれば解ける

# import numpy as np


## test data
# 4
# 3 1 4 2
# 10 20 30 40
## ans=60

# import bisect

class BIT:

	def __init__(self,size):
		self.N = size
		self.bit = [0] * (self.N+1)

	def getSum(self,i):
		s = 0
		while 0 < i:
			s += self.bit[i]
			i -= i & -i

		return s

	def getMax(self,i):
		s = 0
		while 0 < i:
			s = max(s, self.bit[i])
			i -= i & -i

		return s

	def add(self,i,val):
		while i <= self.N:
			# for range summary query
			# self.bit[i] += val
			# for range maximum query
			self.bit[i] = max( self.bit[i], val )
			i += i & -i

def LongestIncreaseSeaquence(H,A):
	# === Coordinate compression ===
	# unique and sort asc
	N = len(H)
	# sortedA = sorted(list(set(A)))
	lis = 0

	# === Range Maximum Query ===
	# ここでは、各要素iに、最後の値がiの時のLISを登録
	tree = BIT(N)
	for n in range(N):
		tree.add( H[n], tree.getMax(H[n]) + A[n] )

	lis = tree.getMax(N)

	return lis


def main():
	N = int(input())
	# 高さは、N以下で全部違うらしい
	H = list(map(int, input().split()))
	A = list(map(int, input().split()))
	# A = [ int(input()) for _ in range(N)]
	print(LongestIncreaseSeaquence(H,A))



if __name__ == "__main__":
	main()
