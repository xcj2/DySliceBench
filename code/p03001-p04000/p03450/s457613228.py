class UnionFind:
    __slots__ = ["nodes", "weight"]
    
    def __init__(self, n: int) -> None:
        self.nodes = [-1]*n
        self.weight = [0]*n
        
    def get_root(self, x:int) -> int:
        if x<0:
            raise ValueError("Negative Index")
        
        if self.nodes[x]<0:
            return x
        else:
            parent, self.nodes[x] = self.nodes[x], self.get_root(self.nodes[x])
            self.weight[x] += self.weight[parent]
            return self.nodes[x]

    def unite(self, x:int, y:int) -> None:
        if x<0 or y<0:
            raise ValueError("Negative Index")
            
        root_x, root_y = self.get_root(x), self.get_root(y)
        if root_x != root_y:
            if self.nodes[root_x] < self.nodes[root_y]:
                bigroot, smallroot = root_x, root_y
            else:
                bigroot, smallroot = root_y, root_x
                
            self.nodes[bigroot] += self.nodes[smallroot]
            self.nodes[smallroot] = bigroot

    def relate(self, smaller:int, bigger:int, diff_weight:int) -> None:
        if smaller<0 or bigger<0:
            raise ValueError("Negative Index")
            
        s_root, b_root = self.get_root(smaller), self.get_root(bigger)
        if s_root == b_root:
            if self.weight[smaller] + diff_weight == self.weight[bigger]:
                return
            raise ValueError
            
        else:
            self.weight[b_root] = diff_weight - self.weight[bigger]
            self.nodes[s_root] += self.nodes[b_root]
            self.nodes[b_root] = smaller
            
   
         
N,M = map(int, input().split())
LRD = []
for _ in range(M):
    LRD.append(tuple(map(int, input().split())))
 
uf = UnionFind(N)
relate = uf.relate    

try:
    for l,r,d in LRD:
        relate(l-1,r-1,d)
    print("Yes")
except Exception as e:
    print("No")