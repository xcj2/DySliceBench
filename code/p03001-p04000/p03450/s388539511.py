class Unionfind():
    def __init__(self, vertexsize):
        self.table = [[-1, 0] for _ in range(vertexsize)]

    def find(self, x):
        dis = 0
        while(self.table[x][0] >= 0):
            dis += self.table[x][1]
            x = self.table[x][0]
        return x, dis

    def union(self, x, y, d):
        xl, xd = self.find(x)
        yl, yd = self.find(y)
        if xl != yl:
            if self.table[xl][0] <= self.table[yl][0]:
                self.table[xl][0] += self.table[yl][0]
                self.table[yl] = [xl, xd + d - yd]
            else:
                self.table[yl][0] += self.table[xl][0]
                self.table[xl] = [yl, -xd - d + yd]
            return True
        else:
            return xd + d == yd

n, m = map(int, input().split())
info = [tuple(map(int, input().split())) for _ in range(m)]
uf = Unionfind(n)
for l, r, d in info:
    ret = uf.union(l-1, r-1, d)
    if not ret:
        print('No')
        exit()
print('Yes')