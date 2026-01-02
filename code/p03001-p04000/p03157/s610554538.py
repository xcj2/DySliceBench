# Union-Findデータ構造
class UnionFind:
    def __init__(self, numV):
        self.pars = list(range(numV))
        self.ranks = [0] * numV
    def find(self, x):
        if self.pars[x] == x: return x
        else:
            self.pars[x] = self.find(self.pars[x])
            return self.pars[x]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return
        if self.ranks[x] < self.ranks[y]:
            self.pars[x] = y
        else:
            self.pars[y] = x
            if self.ranks[x] == self.ranks[y]:
                self.ranks[x] += 1
    def same(self, x, y):
        return self.find(x) == self.find(y)

def conv(i, j):
    return (i-1)*W + j-1

H, W = map(int, input().split())
Sss = ['_' + input() + '_' for _ in range(H)]
Sss = ['_' * (W + 2)] + Sss + ['_' * (W + 2)]

N = H * W
UF = UnionFind(N)
for i in range(1, H+1):
    for j in range(1, W+1):
        revS = '.' if Sss[i][j] == '#' else '#'
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            if Sss[i+di][j+dj] == revS:
                UF.union(conv(i, j), conv(i+di, j+dj))

numBs, numWs = [0]*N, [0]*N
for i in range(1, H+1):
    for j in range(1, W+1):
        no = UF.find(conv(i, j))
        if Sss[i][j] == '#':
            numBs[no] += 1
        else:
            numWs[no] += 1

ans = 0
for numB, numW in zip(numBs, numWs):
    ans += numB * numW
print(ans)
