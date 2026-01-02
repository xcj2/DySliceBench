import sys
input = sys.stdin.readline
'''
allinputs = iter(input().splitlines())
input = lambda : next(allinputs)
#'''

class union_find:
	def __init__(self, num_node):
		self.parent = [-1] * num_node
		
	def root(self, node):
		if self.parent[node] < 0:
			return node
		else:
			self.parent[node] = self.root(self.parent[node])
			return self.parent[node]
			
	def size(self, node):
		return -self.parent[self.root(node)]
		
	def same(self, node1, node2):
		if self.root(node1) == self.root(node2):
			return True
		else:
			return False
			
	def unite(self, node1, node2):
		if self.same(node1, node2):
			return False
		else:
			siz1 = self.size(node1)
			siz2 = self.size(node2)
			if siz1 < siz2:	
				self.parent[self.root(node2)] -= siz1
				self.parent[self.root(node1)] = self.root(node2)
			else:
				self.parent[self.root(node1)] -= siz2
				self.parent[self.root(node2)] = self.root(node1)
			return True
	
def main():
	N, M = map(int, input().split())
	A = [0] * M
	B = [0] * M
	uf = union_find(N)
	
	for i in range(M):
		A[i], B[i] = map(int, input().split())
		A[i] -= 1
		B[i] -= 1
		
	unco = [0] * M
	unco[M - 1] = (N * (N - 1)) // 2
	
	for i in range(M - 1, 0, -1):
		tmp1 = uf.size(A[i])
		if uf.unite(A[i], B[i]):
			tmp2 = uf.size(A[i])
			unco[i - 1] = unco[i] - (tmp2 - tmp1) * tmp1
		else:
			unco[i - 1] = unco[i]
	
	for i in range(M):
		print(unco[i])
		
main()