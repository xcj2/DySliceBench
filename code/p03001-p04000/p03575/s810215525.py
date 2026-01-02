class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if(x == y):
            return
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1

    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    def Count(self, x):
        return -self.root[self.Find_Root(x)]


def is_bridge(n, ab, i):
    uni = UnionFind(n)
    for j, val in enumerate(ab):
        if i == j:
            continue
        else:
            uni.Unite(val[0]-1, val[1]-1)
    if uni.Count(0) == n:
        return False
    else:
        return True


n, m = map(int, input().split())
ab = []
for i in range(m):
    a, b = map(int, input().split())
    ab.append((a, b))

ret = 0

for i in range(m):
    if is_bridge(n, ab, i):
        ret += 1

print(ret)
