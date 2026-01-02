class weight_union_find(object):
    def __init__(self, n):
        self.par = [-1 for i in range(n)]
        self.weight_diff = [0 for i in range(n)]
    
    def root(self, ind):
        if self.par[ind] < 0:
            return ind
        else:
            r = self.root(self.par[ind])
            self.weight_diff[ind] += self.weight_diff[self.par[ind]]
            self.par[ind] = r
            return r

    def unite(self, ind1, ind2, w):
        root1 = self.root(ind1)
        root2 = self.root(ind2)
        if root1 == root2:
            # 重みが違う==解無し
            # print(root1, root2, self.weight_diff[ind1], self.weight_diff[ind2], w)
            if -(self.weight_diff[ind1] - self.weight_diff[ind2]) == w:
                return True
            else:
                return False
        else:
            #swap
            if self.par[root1] > self.par[root2]:
                root1, root2 = root2, root1
                ind1, ind2 = ind2, ind1
                w *= -1
            self.par[root1] += self.par[root2]
            self.par[root2] = root1
            self.weight_diff[root2] = w + self.weight_diff[ind1] - self.weight_diff[ind2]
            return True



n, m = list(map(int, input().split()))
query = []
for i in range(m):
    query.append(list(map(int, input().split())))
uf = weight_union_find(n)
for l, r, d in query:
    if not uf.unite(l-1, r-1, d):
        print("No")
        exit()
print("Yes")