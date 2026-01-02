import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**9)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self,x):
        if(self.parents[x] < 0):
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def size(self, x):
        return self.parents[ self.find(x) ] * -1

    def same(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        return (x_root == y_root)

    def union(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        if(x_root == y_root):
            return

        #　番号が大きい方を新しい根にする
        if( x_root > y_root ):
            self.parents[x_root] += self.parents[y_root]
            self.parents[y_root] = x_root
        else:
            self.parents[y_root] += self.parents[x_root]
            self.parents[x_root] = y_root

    def members(self,x):
        root = self.find(x)
        ret = [ i for i in range(self.n) if self.find(i) == root ]
        return ret

    def roots(self):
        ret = [ i for i in range(self.n) if self.parents[i] < 0]
        return ret

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

n,m = map(int,readline().split())
x = list(map(int,readline().split()))
aby = list(map(int,read().split()))

edges = []
it = iter(aby)
for a,b,y in zip(it,it,it):
    edges.append((y,a,b))
edges.sort()

n_bi = n*2
bitree = [[0,-1,-1,-1,0] for _ in range(n_bi)]
for i,xi in enumerate(x,1):
    bitree[i][0] = xi

uf = UnionFind(n_bi)

e_ind = 0
for i in range(n+1,n_bi):
    while(True):
        e1 = edges[e_ind][1]
        e2 = edges[e_ind][2]
        if(uf.same(e1,e2)):
            e_ind += 1
            continue
        break

    left = uf.find(e1)
    right = uf.find(e2)
    edge_cost = edges[e_ind][0]

    bitree[i] = [bitree[left][0] + bitree[right][0],
                 -1,
                 left,
                 right,
                 edge_cost]
    bitree[left][1] = i
    bitree[right][1] = i

    uf.union(left,i)
    uf.union(right,i)

tree_group = [-1] * (n+1)
tree_group_cost = []
tree_group_ind = -1
stack = [n_bi-1]
while(stack):
    i = stack.pop()
    if(bitree[i][0] >= bitree[i][4]):
        #連結
        tree_group_ind += 1
        tree_group_cost.append(bitree[i][0])
        stack2 = [i]
        while(stack2):
            j = stack2.pop()
            if(j > n):
                stack2.append(bitree[j][2])
                stack2.append(bitree[j][3])
            else:
                tree_group[j] = tree_group_ind
    else:
        #非連結
        stack.append(bitree[i][2])
        stack.append(bitree[i][3])

ans = 0
for y,a,b in edges:
    if(tree_group[a]==tree_group[b]):
        tg = tree_group[a]
        if(tree_group_cost[tg] >= y):
            ans += 1

ans = m - ans
print(ans)