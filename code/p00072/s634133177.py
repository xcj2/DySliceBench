class Wood:
  def __init__(self,noods,edges):
    self.noods = noods
    self.edges = edges
  def cons(self,other):
    self.noods.extend(other.noods)
    self.edges.extend(other.edges)

class Edge:
  def __init__(self,n1,n2,length):
    self.n1 = n1
    self.n2 = n2
    self.length = length

def check(woods,edge):
  w1 = woods[edge.n1]
  w2 = woods[edge.n2]
  if w1.noods!= w2.noods:
    w1.cons(w2)
    w1.edges.append(edge)
    for i in w1.noods:
      woods[i] = w1
while True:
  n = int(input())
  if n == 0:
    break
  m = int(input())
  e = []
  woods = []
  for i in range(m):
    n1,n2,length = map(int,input().split(","))
    edge = Edge(n1,n2,length)
    e.append(edge)
  e = sorted(e,key=lambda x:x.length)

  for i in range(n):
    wood = Wood([i],[])
    woods.append(wood)

  for edge in e:
    check(woods,edge)

  s = 0
  for edge in woods[0].edges:
    s += edge.length//100-1
  print(s)