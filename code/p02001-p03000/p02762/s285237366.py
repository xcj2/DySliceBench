class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
def main():

    n,m,k=map(int,input().split())
    uf=UnionFind(n)
    block={}
    for i in range(n):
        block[i]=[i]
    for i in range(m):
        a,b=map(int,input().split())
        uf.union(a-1,b-1)
        block[a-1].append(b-1)
        block[b-1].append(a-1)
        
    for i in range(k):
        a,b=map(int,input().split())
        block[a-1].append(b-1)
        block[b-1].append(a-1)
    ans=[]
    #print(block)
    for i in range(n):
        res=uf.size(i)
    #   print(res)
        for value in block[i]:
            if uf.same(value,i):
                res-=1
        ans.append(res)
    print(*ans)
        
        
if __name__=="__main__":
    main()
