import sys
input = sys.stdin.buffer.readline

def main():
	
	class BinaryIndexedTree:
		
		# 初期化
		def __init__(self, size, default):
			self.size = size
			self.default = default
			self.BIT = [default]*(self.size+1)

		# function(max, min, plus, minus, etc...)
		def BIT_segfunc(self, x, y):
			return max(x, y)

		def BIT_query(self, idx):
			ret = self.default
			while idx > 0:
				ret = self.BIT_segfunc(ret, self.BIT[idx])
				idx -= idx&(-idx)
			return ret

		# update
		def BIT_update(self, idx, x):
			while idx <= self.size:
				self.BIT[idx] = self.BIT_segfunc(self.BIT[idx], x)
				idx += idx&(-idx)
			return

		def BIT_range(self, x, y):
			return self.BIT_query(y)-self.BIT_query(x)

		# seg確認用
		def BIT_print(self):
			print(self.BIT)
		
	N = int(input())
	a = list(map(int,input().split()))
	l = [0]*N;r = [0]*N
	left_bit = BinaryIndexedTree(N, 0)
	for i, num in enumerate(a):
	    l[num-1] = i + 1 - left_bit.BIT_query(num)
	    left_bit.BIT_update(num, i+1)
	right_bit = BinaryIndexedTree(N, 0)
	for i, num in enumerate(a[::-1]):
	    r[num-1] = i + 1 - right_bit.BIT_query(num)
	    right_bit.BIT_update(num, i+1)
	
	print(sum(l[i]*r[i]*(i+1) for i in range(N)))

if __name__ == "__main__":
	main()
