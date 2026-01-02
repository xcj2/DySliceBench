class Element:
	val = 0
	parent = None
	height = 0
	size = 1
	def __init__(self, val, parent=None, height=0, size=1):
		self.val = val
		if parent is None:
			self.parent = self
		else:
			self.parent = parent
		self.height = height
		self.size = size

class UnionFindTree:
	elemnts = []

	def __init__(self, n):
		self.elemnts = [Element(val=i) for i in range(n)]

	def root(self, x:int) -> Element:
		if self.elemnts[x].parent is self.elemnts[x]:
			return self.elemnts[x]
		return self.root(self.elemnts[x].parent.val)

	def same(self, x:int, y:int) -> bool:
		rx = self.root(x)
		ry = self.root(y)
		return rx is ry

	def unite(self, x:int, y:int):
		rx = self.root(x)
		ry = self.root(y)
		if rx == ry:
			return
		if rx.height < ry.height:
			rx.parent = ry
			ry.size += ry.height
		else:
			ry.parent = rx
			rx.size += ry.size
			if rx.height == ry.height:
				rx.height += 1

def main():
	N, M = map(int, input().split())
	uionfind = UnionFindTree(N)
	for i in range(M):
		u, v, z = map(int, input().split())
		uionfind.unite(u-1, v-1)
	ans_set = set()

	ans = 0
	for i in range(N):
		this_root = uionfind.root(i).val
		if not this_root in ans_set:
			ans += 1
			ans_set.add(this_root)
	print(ans)


if __name__ == '__main__':
	main()