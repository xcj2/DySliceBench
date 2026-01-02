__author__ = 'zhewang711'
import sys
sys.setrecursionlimit(200000)
class Graph:
    def __init__(self):
        self.vertices = 0
        self.outgoing = {}
        self.root_cnt = 0
        # self.incoming = {}
        self.result = set()

    def insert_vertice(self):
        self.vertices += 1
        self.outgoing[self.vertices - 1] = []
        # self.incoming[self.vertices - 1] = {}

    def insert_edge(self, s, d):
        if s >= self.vertices or d >= self.vertices:
            raise ValueError('edge cannot be inserted because vertex do not exist')
        else:
            self.outgoing[s].append(d)
            self.outgoing[d].append(s)

    def get_input(self):
        s = input()
        V, E = int(s.split()[0]), int(s.split()[1])
        self.discovery = [None for i in range(V)]
        self.clock = 0
        self.explored = [False for i in range(V)]
        self.father = [None for i in range(V)]
        self.backing = [None for i in range(V)]
        self.sub_have_backing = [None for i in range(V)]
        self.is_leaf = [None for i in range(V)]
        for i in range(V):
            self.insert_vertice()
        for i in range(E):
            s = input()
            self.insert_edge(int(s.split()[0]), int(s.split()[1]))



    def read_input(self, filename):
        f = open(filename, 'r')
        cnt = 0
        for line in f:
            if cnt == 0:
               cnt += 1
               V, E = int(line.split()[0]), int(line.split()[1])

               self.discovery = [None for i in range(V)]
               self.clock = 0
               self.explored = [False for i in range(V)]
               self.father = [None for i in range(V)]
               self.backing = [None for i in range(V)]
               self.sub_have_backing = [False for i in range(V)]
               self.is_leaf = [None for i in range(V)]

               for i in range(V):
                   self.insert_vertice()
            else:
                self.insert_edge(int(line.split()[0]), int(line.split()[1]))

    def DFS(self, root):
        self.explored[root] = True
        self.discovery[root] = self.clock
        self.backing[root] = self.clock
        self.clock += 1
        self.is_leaf[root] = True
        for ver in self.outgoing[root]:
            if not self.explored[ver]:
                self.is_leaf[root] = False
                self.DFS(ver)
                self.backing[root] = min(self.backing[root], self.backing[ver])
            else:
                self.backing[root] = min(self.backing[root], self.discovery[ver])

    def _critical_points(self, root):
        self.explored[root] = True
        self.discovery[root] = self.clock
        self.clock += 1
        for ver in self.outgoing[root]:
            if not self.explored[ver]:
                if root == 0:
                    self.root_cnt += 1
                if self.backing[ver] >= self.discovery[root] and root !=0 and not self.is_leaf[root]:
                    self.result.add(root)
                self._critical_points(ver)

g = Graph()
g.get_input()
#g.read_input('1.txt')
g.DFS(0)
g.clock = 0
g.discovery = [None for i in range(g.vertices)]
g.explored = [False for i in range(g.vertices)]
g._critical_points(0)
if g.root_cnt >= 2:
    g.result.add(0)
l = sorted(g.result)
for i in l:
    print(i)