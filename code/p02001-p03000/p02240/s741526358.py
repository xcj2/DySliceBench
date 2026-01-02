class Vertex:
	def __init__(self):
		self.c = 0
		self.vertices = []
	def add(self, u):
		self.vertices.append(u)

def dfs(vertices):
	c = 0
	for i in range(len(vertices)):
		c += 1
		if vertices[i].c == 0:
			vertices[i].c = c
			stack = []
			stack.append(i)
			while len(stack) != 0:
				cur = vertices[stack.pop()]
				for j in range(len(cur.vertices)):
					u = cur.vertices[j]
					if vertices[u].c == 0:
						vertices[u].c = c
						stack.append(u)
	return

n, m = map(int, input().split())
vertices = []
for i in range(n):
	vertices.append(Vertex())
for i in range(m):
	u1, u2 = map(int, input().split())
	vertices[u1].add(u2)
	vertices[u2].add(u1)

dfs(vertices)

q = int(input())
for i in range(q):
	u1, u2 = map(int, input().split())
	if vertices[u1].c == vertices[u2].c:
		print('yes')
	else:
		print('no')

