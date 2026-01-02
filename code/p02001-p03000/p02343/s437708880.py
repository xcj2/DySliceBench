#! /usr/local/bin/python

class N:
	def __init__(self, n):
		self.parent = n
		self.rank = 0
		self.n = n

def find( n: int) -> N:
	if data[n].parent == n:
		return data[n]
	else:
		data[n].parent = find(data[n].parent).n
		return data[data[n].parent]

def union( a: int, b: int):
	A = find(a)
	B = find(b)
	if A.rank > B.rank:
		B.parent = A.n
	elif A.rank < B.rank:
		A.parent = B.n
	elif A.n != B.n:
		B.parent = A.n
		A.rank = A.rank + 1

# Start
n, p = input().split(" ")
data = [ N(i) for i in range(int(n))]
for i in range(int(p)):
	com, x, y = input().split(" ")
	if com == '0':
		union(int(x),int(y))
	else:
		if find(int(x)).n != find(int(y)).n:
			print(0)
		else:
			print(1)