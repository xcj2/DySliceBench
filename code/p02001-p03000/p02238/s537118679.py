time = 1

class Vertex:
	def __init__(self, u, k):
		self.u = u
		self.vertices = [0] * k
		self.d = self.f = 0
	def __str__(self):
		return str(self.u) + ' ' + str(self.d) + ' ' + str(self.f)

def DFS(n, vertices):
	for i in range(n):
		if vertices[i].d == 0:
			DFS_(vertices, vertices[i].u)
			
def DFS_(vertitces, u):
	vertex = vertices[u-1]
	if vertex.d == 0:
		global time
		vertex.d = time
		time += 1
		for i in range(len(vertex.vertices)):
			DFS_(vertices, vertex.vertices[i])
		vertex.f = time
		time += 1
	
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

DFS(n, vertices)
for i in range(n):
	print(str(vertices[i]))

