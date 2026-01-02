import sys
input = sys.stdin.readline


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rnk = [0] * (n + 1)

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

    def size(self, x):
        return -self.root[self.find_root(x)]


def main():
    N = int(input())
    xy_list = []
    x_list = []
    y_list = []
    for i in range(N):
        x, y = map(int, input().split())
        xy_list.append((x, y))
        x_list.append(x)
        y_list.append(y)

    x_list = list(set(x_list))
    y_list = list(set(y_list))
    x_list.sort()
    y_list.sort()
    dictX = {}
    dictY = {}
    for i, x in enumerate(x_list):
        dictX[x] = i
    for i, y in enumerate(y_list):
        dictY[y] = i

    xy_c = [[] for _ in range(len(x_list))]
    for x, y in xy_list:
        xc, yc = dictX[x], dictY[y]
        xy_c[xc].append(yc)

    UF = UnionFind(len(y_list) + 1)
    for i in range(len(x_list)):
        j_list = xy_c[i]
        if len(j_list) > 1:
            j0 = j_list[0]
            for j in j_list[1:]:
                UF.unite(j0, j)

    ans = 0
    for i in range(len(x_list)):
        j0 = xy_c[i][0]
        ans += UF.size(j0) - len(xy_c[i])
    print(ans)


if __name__ == '__main__':
    main()
