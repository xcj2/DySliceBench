from collections import defaultdict
import sys
sdin = sys.stdin.readline

class UnionFind:
    def __init__(self, node:int) -> None:
        self.n = node
        self.par = [i for i in range(self.n)]
        self.rank = [0 for i in range(self.n)]
        
    def find(self, x:int) -> int:
        if x == self.par[x]:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
        
    def unite(self, x:int, y:int) -> bool:
        if self.isSame(x,y):
            #print("x and y has already united")
            return False
        
        rx = self.find(x)
        ry = self.find(y)
        
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
        else:
            self.par[ry] = rx
            
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
                
        return True
    
    def isSame(self, x:int, y:int) -> bool:
        return self.find(x) == self.find(y)

    

        
N, M = map(int, sdin().split())
P = list(map(int, sdin().split()))
XY = []
for i in range(M):
    XY.append(list(map(int, sdin().split())))


root_node = defaultdict(list)

uf = UnionFind(N)
for x,y in XY:
    x -= 1
    y -= 1
    uf.unite(x,y)

for i in range(N):
    uf.find(i)
    
par = uf.par

for i,root in enumerate(par):
    root_node[root].append(i)
    
ans = 0
for node_list in root_node.values():
    num_list = []
    for i in node_list:
        num_list.append(P[i]-1)
    
    ans += len(set(node_list)&set(num_list))
            
print(ans)
