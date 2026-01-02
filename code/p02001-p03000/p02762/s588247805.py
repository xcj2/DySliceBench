import sys
from collections import deque

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

def main():
	N,M,K = MI()
	frend = [[] for _ in range(N)]
	block = [[] for _ in range(N)]
	uf = UnionFind(N)
	for _ in range(M):
		A,B = map(int1, sys.stdin.readline().split())
		uf.union(A,B)
		frend[A].append(B)
		frend[B].append(A)

	for _ in range(K):
		C,D = map(int1, sys.stdin.readline().split())
		if uf.same(C,D):
			block[C].append(D)
			block[D].append(C)

	ans_v = []
	for i in range(N):
		ans = uf.size(i)-len(frend[i])-len(block[i])-1
		ans_v.append(ans)
	printH(ans_v)

main()