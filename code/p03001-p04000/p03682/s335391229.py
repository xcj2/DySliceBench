from operator import itemgetter
import heapq

N = int(input())
X = [[int(p) for p in input().split()] for _ in range(N)]

X.sort()
for i in range(N):
    X[i].append(i)
    
Y = sorted(X, key=itemgetter(1))

h = []
for i in range(N-1):
    heapq.heappush(h, (X[i+1][0]-X[i][0], i+1, i))
    heapq.heappush(h, (Y[i+1][1]-Y[i][1], Y[i+1][2], Y[i][2]))
    
    
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)
        
    def find_root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]
        
    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1
                
    def isSameGroup(self, x, y):
        return self.find_root(x) == self.find_root(y)
    
    def count(self, x):
        return -self.root[self.find_root(x)]
    
    
UF = UnionFind(N)
ans = 0
while h:
    t = heapq.heappop(h)
    if UF.isSameGroup(t[1], t[2]):
        continue
    ans += t[0]
    UF.unite(t[1], t[2])
    
print(ans)