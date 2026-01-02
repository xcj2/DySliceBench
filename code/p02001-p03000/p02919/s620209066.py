import sys
input = sys.stdin.buffer.readline

def main():
	N = int(input())
	p = list(map(int,input().split()))
	nl = [0]*N
	for i,num in enumerate(p):
		nl[num-1] = i+1
	nl.reverse()
	
	class BinaryIndexedTree:
		
		# 初期化
		def __init__(self, size, default):
			self.size = size
			self.default = default
			self.BIT = [default]*(self.size+1)
 
		# function(max, min, plus, minus, etc...)
		def BIT_segfunc(self, x, y):
			return x+y
 
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
 
		# BIT確認用
		def BIT_print(self):
			print(self.BIT)
			
		def BIT_search(self, x):
			i = 0
			s = 0
			step = 1<<(self.size.bit_length()-1)
			while step:
				if i+step <= self.size and s + self.BIT[i+step] < x:
					i += step
					s += self.BIT[i]
				step >>= 1
			return i+1
	
	BIT = BinaryIndexedTree(N, 0)
	ans = 0
	for i,num in enumerate(nl):
		l = BIT.BIT_query(num)
		BIT.BIT_update(num, 1)
		r = i-l
		a = BIT.BIT_search(l-1) if l >= 2 else 0
		b = BIT.BIT_search(l) if l >= 1 else 0
		d = BIT.BIT_search(l+2) if r >= 1 else N+1
		e = BIT.BIT_search(l+3) if r >= 2 else N+1
		ret = 0
		if b != 0:
			ret += (b-a)*(d-num)
		if d != 0:
			ret += (e-d)*(num-b)
		ans += ret*(N-i)
	print(ans)
	
if __name__ == "__main__":
	main()