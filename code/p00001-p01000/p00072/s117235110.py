class Wood:
  def __init__(self,num,noods,edges):
    self.num = num
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
  if woods[edge.n1].num != woods[edge.n2].num:
    woods[edge.n1].cons(woods[edge.n2])
    woods[edge.n1].edges.append(edge)
    for i in woods[edge.n1].noods:
      woods[i] = woods[edge.n1]
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
    wood = Wood(i,[i],[])
    woods.append(wood)
  for edge in e:
    check(woods,edge)
  s = 0
  for edge in woods[0].edges:
    s += edge.length//100-1
  print(s)