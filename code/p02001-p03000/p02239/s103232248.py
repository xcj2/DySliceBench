from queue import *

class Vertex:
	def __init__(self, u, k):
		self.u = u
		self.vertices = [0] * k
		self.d = -1
	def __str__(self):
		return str(self.u) + ' ' + str(self.d)

class Inf:
	def __init__(self,u,d):
		self.u = u
		self.d = d

def BFS(n, vertices):
	q = Queue()
	q.put(Inf(1,0))
	while q.empty() == False:
		inf = q.get()
		vertex = vertices[inf.u-1]
		if vertex.d == -1:
			vertex.d = inf.d
		else:
			vertex.d = min(vertex.d, inf.d)
		dist = inf.d + 1
		for i in range(len(vertex.vertices)):
			u = vertex.vertices[i]
			if vertices[u-1].d == -1:
				q.put(Inf(u, dist))
	
n = int(input())
vertices = []
for i in range(n):
	v = list(map(int, input().split()))
	u = v[0]
	k = v[1]
	vertex = Vertex(u, k)
	for j in range(k):
		vertex.vertices[j] = v[j+2]
	vertices.append(vertex)

BFS(n, vertices)
for i in range(n):
	print(str(vertices[i]))
