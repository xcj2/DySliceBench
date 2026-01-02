import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
printV = lambda x: print(*x, sep="\n")
printH = lambda x: print(" ".join(map(str,x)))
def IS(): return sys.stdin.readline()[:-1]
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LII(rows_number): return [II() for _ in range(rows_number)]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]

class UnionFind():
	def __init__(self, n):
		self.n=n
		self.parents = [-1]*n
	def find(self, x):
		if self.parents[x] < 0:
			return x
		else:
			self.parents[x] = self.find(self.parents[x])
			return self.parents[x]
	def union(self,x,y):
		x = self.find(x)
		y = self.find(y)
		if x==y:
			return
		if self.parents[x] > self.parents[y]:
			x, y = y, x
		self.parents[x] += self.parents[y]
		self.parents[y] = x
	def size(self, x):
		return -self.parents[self.find(x)]
	def same(self, x, y):
		return self.find(x) == self.find(y)
	def members(self, x):
		root = self.find(x)
		return [i for i in range(self.n) if self.find(i) == root]
	def roots(self):
		return [i for i, x in enumerate(self.parents) if x < 0]
	def group_count(self):
		return len(self.roots())
	def all_group_members(self):
		return {r: self.members(r) for r in self.roots()}
	def __str__(self):
		return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
	N,M = MI()
	pp = LI1()
	uf = UnionFind(N)
	for _ in range(M):
		x,y = MI()
		x-=1
		y-=1
		uf.union(x,y)

	ans = 0
	for i,p in enumerate(pp):
		if(uf.same(i,p)):
			ans+=1
	print(ans)




if __name__ == '__main__':
	main()