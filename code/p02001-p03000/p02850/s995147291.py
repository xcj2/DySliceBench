import sys
sys.setrecursionlimit(1000000)
N = int(input())

class vertex:
  def __init__(self,i):
    self.__i = i
    self.__e = []
    self.__d = 0
    self.__nei = []
  def add_e(self, e):
    self.__e.append(e)
    self.__d += 1
    self.__nei.append(e.get_pair_v(self.__i))
  def get_e(self):
    return self.__e
  def get_d(self):
    return self.__d
  def get_i(self):
    return self.__i
  def get_n(self):
    return self.__nei
  
class edge:
  def __init__(self, i, a, b):
    self.__i = i
    self.__c = -1
    self.__v = dict()
    self.__v[a] = b
    self.__v[b] = a
  def get_pair_v(self, a):
    return self.__v[a]
  def get_c(self):
    return self.__c
  def set_c(self, a):
    if self.__c == -1:
      self.__c = a
      return True
    else:
      return False
  def get_i(self):
    return self.__i
    
class tree:
  def __init__(self,N):
    self.__v = [vertex(i) for i in range(N+1)]
    self.__e = []
    self.__max_d = 0
    self.__max_v_idx = 0
    
  def add_e(self,i, a, b):
    ed = edge(i, a, b)
    self.__e.append(ed) 
    self.__v[a].add_e(ed)
    self.__v[b].add_e(ed)
  
  def reload_max_d(self):
    for i in self.__v:
      if i.get_d() > self.__max_d:
        self.__max_d = i.get_d()
        self.__max_v_idx = i.get_i()
        
  def painting(self):
    v = self.__max_v_idx
    edges = self.__v[v].get_e()
    for i, ver in enumerate(edges):
      ver.set_c(i+1)
      self.change_c(ver.get_pair_v(v),ver)   
    
  def change_c(self, idx, prev_e):
    edges = self.__v[idx].get_e()
    edges.remove(prev_e)
    offset = 0
    prev_e_c = prev_e.get_c()
    if not edges:
      return
    for ver in edges:
      offset += 1
      if offset == prev_e_c:
        offset += 1
      if ver.set_c(offset):
        self.change_c(ver.get_pair_v(idx),ver)   
  
  def show_max_d(self):
    print(self.__max_d)
    
  def show_colors(self):
    for i in self.__e:
      print(i.get_c()) 

t = tree(N)
for i in range(N-1):
  temp = list(map(int, input().split()))
  t.add_e(i, temp[0], temp[1])
t.reload_max_d()
t.painting()
t.show_max_d()
t.show_colors()

