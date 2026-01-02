N, M = map(int, input().split())
XYZ = []
for _ in range(M):
    x,y,z = map(int, input().split())
    XYZ.append((x,y,z))
    
pairs = XYZ[:]
known = [False] * (N)

pairs = sorted(pairs)

# UnionFindの元
class UnionFind:
    def __init__(self, n):
        # n : ノード数（ノード番号は0始まり）
        self.par = [i for i in range(n)] # 各ノードの親
        self.rank = [0] * n              # 各木の高さ
        
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
        
    def is_group(self, x, y):
        return self.find(x) == self.find(y)
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

# UnionFindでグループ化
def create_union(edges, v_num):
    # edges: 辺
    # v_num: ノード数
    u = UnionFind(v_num)
    for x,y in edges:
        u.union(x,y)
        
    return [u.find(x) for x in range(v_num)]
     
    
edges = [(x,y) for x,y,z in pairs]

parents = create_union(edges, N+1)
union = set()
for p in parents:
    union.add(p)
union_num = len(union) -1
print(union_num)


