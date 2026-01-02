import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

class DSU(object):
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.cycle = False

    def find(self, key):
        if self.parent[key] != key:
            self.parent[key] = self.find(self.parent[key])
        return self.parent[key]

    def union(self, a, b):
        s1, s2 = self.find(a), self.find(b)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
                self.rank[s2] += self.rank[s1]
            else:
                self.parent[s2] = s1
                self.rank[s1] += self.rank[s2]
        else:
            self.cycle = True
        
    def has_cycle(self):
        return self.cycle
    
    def show_parent(self):
        return self.parent

    def show_rank(self):
        return self.rank

def solve():
    n, m = map(int, input().split())
    d = DSU(n + 1)
    if m > 0:
        for _ in range(m):
            a, b = map(int, input().split())
            d.union(a, b)
        # print(d.show_parent())
        print(max(d.show_rank()))
    else:
        print(1)

solve()