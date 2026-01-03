

def main():
    import sys
    input = sys.stdin.readline

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
            arr=[]
            for r in range(self.roots()):
                arr.append(set(self.members(r)))
            return arr

        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
    
################
    mod=10**9+7
    N,K,L=MI()
    uf1 = UnionFind(N)
    uf2 = UnionFind(N)
    ans=[0]*N

    for i in range(K):
        p,q=MI()
        p-=1
        q-=1
        uf1.union(p,q)
        
    for i in range(L):
        p,q=MI()
        p-=1
        q-=1
        uf2.union(p,q)
        
    from collections import defaultdict
    dd = defaultdict(int)
    
    for i in range(N):
        a=uf1.find(i)
        b=uf2.find(i)
        dd[(a,b)]+=1
        
    for i in range(N):
        a=uf1.find(i)
        b=uf2.find(i)
        ans[i]=dd[(a,b)]
        
    print(' '.join(map(str, ans)))
    
    
    
        
        
    


main()
