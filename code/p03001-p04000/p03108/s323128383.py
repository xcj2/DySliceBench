import sys
input = sys.stdin.readline

################
class UnionFind():
    """
    parents : 親要素(findしない場合は根ではないことの注意)，根の場合は"-(要素数）"
    find(x):要素xの属するグループの根を返す
    size(x):要素xの属するグループの要素数を返す
    same(x,y):x,yが同じグループに属しているか返す
    members(x):要素xが属するグループに属する要素をリストで返す
    roots(x):全ての根の要素を返す
    group_counte():グループの数を返す
    all_group_members():{根要素：[そのグループに含まれる要素のリスト]}の辞書を返す
    """
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
    
################

N,M=map(int,input().split())
A=[0]*M
B=[0]*M
ans=[0]*M
for i in range(M):
    a,b=map(int,input().split())
    A[i]=a-1
    B[i]=b-1
    
def cmb(n):
    return n*(n-1)//2
    
uf = UnionFind(N)
ans[-1]=(N*(N-1))//2
for i in range(M-1,0,-1):
    if uf.find(A[i]) !=uf.find(B[i]):
        ga=uf.size(A[i])
        gb=uf.size(B[i])
        ans[i-1]=ans[i]-cmb(ga+gb)+cmb(ga)+cmb(gb)
        uf.union(A[i],B[i])
        if ans[i-1]==0:
            break
    else:
        ans[i-1]=ans[i]
    
for i in range(M):
    print(ans[i])