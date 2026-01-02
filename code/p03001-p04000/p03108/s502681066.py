from itertools import combinations

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
            self.size[x] = self.size[y]
        else:
            if x != y:
                self.size[x] += self.size[y]
                self.size[y] = self.size[x] 
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

def combi(root_list):
    return sum([a*b for a, b in combinations(root_list, 2)])
    
if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    
    AB = AB[::-1]
    
    
    inconvinience = []
    inconvinience.append(N*(N-1)//2)
    
    tree = UnionFind(N)
    for a, b in AB:
        delta = 0
        if not tree.same_check(a, b):
            delta = tree.size[tree.find(a)]*tree.size[tree.find(b)]
        tree.union(a, b)
        inconvinience.append(inconvinience[-1] - delta)
    
    inconvinience.pop()
    
    for i in inconvinience[::-1]:
        print(i)