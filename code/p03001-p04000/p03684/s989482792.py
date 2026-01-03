
class uf_tree():

    def __init__(self,n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def indep(self):
        dep =0
        for i in range(self.n):
            if i == self.par[i]:
                dep += 1

        return dep

    def unite(self,x,y):
        if self.root(x) == self.root(y):
            return
        else:
            rootx = self.root(x)
            rooty = self.root(y)
            if self.rank[rootx] < self.rank[rooty]:
                self.par[rootx] = rooty
            else:
                self.par[rooty] = rootx
                if self.rank[rootx] == self.rank[rooty]:
                    self.rank[rootx] += 1
    def root(self,i):
        if self.par[i] == i:
            return i
        else:
            self.par[i] = self.root(self.par[i])
            return self.par[i]

    def same(self,x,y):
        return self.root(x) == self.root(y)

def kruscal(n,edge_arr):
    edge_arr.sort(key=lambda x:x[2])
    ans = []
    tree = uf_tree(n)
    for e in edge_arr:
        s = e[0]-1
        g = e[1]-1
        if tree.same(s,g):
            continue
        else:
            ans.append(e)
            tree.unite(s,g)
    return ans

p = []
edge = []
n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    p.append([x,y,i+1])

p.sort(key = lambda x:x[0])
for i in range(n-1):
    cost = min(abs(p[i+1][0]-p[i][0]),abs(p[i+1][1]-p[i][1]))
    edge.append([p[i][2],p[i+1][2],cost])

p.sort(key = lambda x:x[1])
for i in range(n-1):
    cost = min(abs(p[i+1][0]-p[i][0]),abs(p[i+1][1]-p[i][1]))
    edge.append([p[i][2],p[i+1][2],cost])

ans = kruscal(n,edge)
tot = 0
for e in ans:
    tot += e[2]
print(tot)