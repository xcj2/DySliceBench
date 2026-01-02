class SegmentTree:
	def __init__(self, orig, func, unit):
		_len = len(orig)
		self.func = func
		self.size = 1 << (_len - 1).bit_length()
		self.tree = [unit] * self.size + orig + [unit] * (self.size - _len)
		self.unit = unit

		for i in range(self.size - 1, 0, -1):
			self.tree[i] = func(self.tree[i * 2], self.tree[i * 2 + 1])

	def update(self, i, v):
		i += self.size
		self.tree[i] = v
		while i:
			i //= 2
			self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])

	def find(self, l, r):
		l += self.size
		r += self.size
		ret = self.unit
		while l < r:
			if l & 1:
				ret = self.func(ret, self.tree[l])
				l += 1
			if r & 1:
				r -= 1
				ret = self.func(ret, self.tree[r])
			l //= 2
			r //= 2
		return ret


def main():
	N, Q, *L = map(int, open(0).read().split())
	tree = SegmentTree([(1 << 31) - 1] * N, min, (1 << 31) - 1)
	ans = []
	for c, x, y in zip(*[iter(L)] * 3):
		if c:
			ans.append(tree.find(x, y + 1))
		else:
			tree.update(x, y)
	print(*ans, sep="\n")


if __name__=="__main__":
	main()

