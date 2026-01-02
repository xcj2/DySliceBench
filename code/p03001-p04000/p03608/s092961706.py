from itertools import permutations
class WarshallFloyd:
    def __init__(self,n):
        self.n = n
        self.inf = float('inf')
        self.d = [[self.inf for _ in range(n)] for _ in range(n)]
        for i in range(self.n):
            self.d[i][i] = 0
    def register(self,v1,v2,l,multiple=True):
        self.d[v1][v2] = l
        if multiple:
            self.d[v2][v1] = l
    def solve(self):
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    self.d[j][k] = min(self.d[j][k],self.d[j][i]+self.d[i][k])
        return self.d
N,M,R = map(int,input().split())
v = list(map(int,input().split()))
Edges = [[] for i in range(N)]
W = WarshallFloyd(N)
for i in range(M):
    a,b,c = map(int,input().split())
    a,b = a-1,b-1
    W.register(a,b,c)
D = W.solve()
a = permutations(v,R)
ans = 100000000000
for e in a:
    value = 0
    for e1,e2 in zip(e[:-1],e[1:]):
        value += D[e1-1][e2-1]
    ans = min(ans,value)
print(ans)