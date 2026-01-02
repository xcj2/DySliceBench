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
    N, M, K = map(int, input().split())
    friend = UnionFind(N)
    direct_friend = [0] * N
    block = [0] * N

    for _ in range(M):
        a, b = map(int, input().split())
        friend.union(a-1, b-1)
        direct_friend[a-1] += 1
        direct_friend[b-1] += 1
    
    for _ in range(K):
        c, d = map(int, input().split())
        if friend.same(c-1, d-1):
            block[c-1] += 1
            block[d-1] += 1

    for i in range(N):
        print(friend.size(i) - direct_friend[i] - block[i] - 1, end=" ")

if __name__ == "__main__":
    main()