
import sys
def input():
	return sys.stdin.readline().strip()




class Union_Find():
	def __init__(self, n):
		self.union = [i for i in range(n)]
		self.level = [0 for i in range(n)]

	def root(self, i, mode=0):
		keiro = [i]
		ans = i
		while ans != self.union[ans]:
			ans = self.union[ans]
			keiro.append(ans)
		if mode == 0:
			return ans
		else:
			return ans, keiro

	def unite(self, i, j):
		root_i, list_i = self.root(i, 1)
		root_j, list_j = self.root(j, 1)
		if root_i != root_j:
			if self.level[root_i] < self.level[root_j]:
				self.level[root_j] = max(self.level[root_i] + 1, self.level[root_j])
				for node in list_i:
					self.union[node] = root_j
			else:
				self.level[root_i] = max(self.level[root_j] + 1, self.level[root_i])
				for node in list_j:
					self.union[node] = root_i

N, K, L = list(map(int, input().split()))

UF_road = Union_Find(N)
UF_train = Union_Find(N)
for i in range(K):
	p, q = list(map(int, input().split()))
	p -= 1
	q -= 1
	UF_road.unite(p,q)
for i in range(L):
	p, q = list(map(int, input().split()))
	p -= 1
	q -= 1
	UF_train.unite(p,q)

group = []
for i in range(N):
	group.append([UF_road.root(i), UF_train.root(i), i])
group.append([100000000,0,0])
group.sort()
X = group[0][0:2]
town = [group[0][2]]
number = [-1 for i in range(N)]
for i in range(1, N + 1):
	if X != group[i][0:2]:
		num = len(town)
		for j in town:
			number[j] = num
		town = [group[i][2]]
	else:
		town.append(group[i][2])
	X = group[i][0:2]


def list_print(A):
	length = len(A)
	for i in range(length - 1):
		print(A[i], end="")
		print(" ", end="")
	print(A[N - 1])

list_print(number)