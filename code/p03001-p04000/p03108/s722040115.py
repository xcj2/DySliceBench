class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            if self.same_check(x, y) != True:
                self.size[y] += self.size[x]
                self.size[x] = 0
            self.par[x] = y
        else:
            if self.same_check(x, y) != True:
               self.size[x] += self.size[y]
               self.size[y] = 0
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
               self.rank[x] += 1

    def siz(self, x):
        x = self.find(x)
        return self.size[x]

def getlist():
	return list(map(int, input().split()))

N, M = getlist()
X = []
for i in range(M):
	A, B = getlist()
	X.append([A, B])

ansL = [0]
ans = 0
UF = UnionFind(N)
for i in range(M - 1):
	x, y = X[-1 - i][0], X[-1 - i][1]
	if UF.same_check(x, y) != True:
		a = UF.size[UF.find(x)]
		b = UF.size[UF.find(y)]
		ans -= a * (a - 1) // 2 + b * (b - 1) // 2
		UF.union(x, y)
		ans += (a + b) * (a + b - 1) // 2
	ansL.append(ans)
	
for i in range(M):
	print(N * (N - 1) // 2 - ansL[-1 - i])