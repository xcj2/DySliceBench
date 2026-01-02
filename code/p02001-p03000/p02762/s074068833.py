class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n
        
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
            return None
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        
    def size(self, x):
        return - self.parents[self.find(x)]
    
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


from collections import defaultdict
 
n, m, k = map(int, input().split())
uf = UnionFind(n+1)
friends = defaultdict(int)
block = defaultdict(int)

# Union-Find木を構築する+各人の直接の友達の数を数える
for _ in range(m):
    a, b = map(int, input().split())
    uf.union(a, b)
    friends[a] += 1
    friends[b] += 1

# Union-Find構造で同じグループに属している(友達の友達or友達の友達の友達or...)場合は、
# ブロック候補として数える(同じグループでない場合は、そもそも友達候補ではない)
for _ in range(k):
    c, d = map(int, input().split())
    if uf.find(c) == uf.find(d):
        block[c] += 1
        block[d] += 1

# 同じグループの人数から、直接の友達の数、ブロック候補の数(別グループの人は含まない)、
# そして、自分の分を差し引けば、友達候補の数を求められる
ans = []
for i in range(1, n+1):
    group_sise = uf.size(i)
    friend_size = friends[i]
    block_size = block[i]
    ans.append(group_sise - friend_size - block_size - 1)
print(*ans)