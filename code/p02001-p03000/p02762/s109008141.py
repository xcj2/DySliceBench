#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

################
class UnionFind():
    """
    parents : 親要素(findしない場合は根ではないことの注意)，根の場合は"-(要素数）"
    find(x):要素xの属するグループの根を返す
    size(x):要素xの属するグループの要素数を返す
    same(x,y):x,yが同じグループに属しているか返す
    members(x):要素xが属するグループに属する要素をリストで返す
    roots:全ての根の要素を返す
    group_count():グループの数を返す
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

def main():
    mod=10**9+7
    N,M,K=MI()
    uf = UnionFind(N)
    cnt=[0]*N#友達の数
    for i in range(M):
        a,b=MI()
        a-=1
        b-=1
        cnt[a]+=1
        cnt[b]+=1
        uf.union(a,b)
        
    blo=[0]*N#同じユニオン内でブロックしているかず
    for i in range(K):
        c,d=MI()
        c-=1
        d-=1
        if uf.same(c,d):
            blo[c]+=1
            blo[d]+=1
    ans=[0]*N    
    for i in range(N):
        ans[i]=uf.size(i) - cnt[i]-blo[i]-1
        
    print(' '.join(map(str, ans)))
        
    

main()
