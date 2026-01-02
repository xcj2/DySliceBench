from operator import itemgetter

class UnionFindTree():
    def __init__(self, N):
        self.__parent_of = [None] * N
        self.__rank_of = [0] * N
        self.__size = [1] * N

    def root(self, value):
        if self.__parent_of[value] is None:
            return value
        else:
            self.__parent_of[value] = self.root(self.__parent_of[value])
            return self.__parent_of[value]

    def unite(self, a, b):
        r1 = self.root(a)
        r2 = self.root(b)
        if r1 != r2:
            if self.__rank_of[r1] < self.__rank_of[r2]:
                self.__parent_of[r1] = r2
                self.__size[r2] += self.__size[r1]
            else:
                self.__parent_of[r2] = r1
                self.__size[r1] += self.__size[r2]
                if self.__rank_of[r1] == self.__rank_of[r2]:
                    self.__rank_of[r1] += 1

    def is_same(self, a, b):
        return self.root(a) == self.root(b)

    def size(self, a):
        return self.__size[self.root(a)]

    def groups(self):
        groups = {}
        for k in range(len(self.__parent_of)):
            r = self.root(k)
            if r not in groups:
                groups[r] = []
            groups[r].append(k)
        return [groups[x] for x in groups]


def main():
    N = int(input())
    uft = UnionFindTree(N)
    P = [None] * N
    for i in range(N):
        x, y = map(int, input().split())
        P[i] = (i, x, y)
    Q = sorted(P, key=itemgetter(1))
    for i in range(1, N):
        if Q[i-1][1] == Q[i][1]:
            uft.unite(Q[i-1][0], Q[i][0])
    R = sorted(P, key=itemgetter(2))
    for i in range(1, N):
        if R[i-1][2] == R[i][2]:
            uft.unite(R[i-1][0], R[i][0])
    groups = uft.groups()
    ans = 0
    for g in groups:
        if len(g) < 3:
            continue
        xs = set()
        ys = set()
        for i in g:
            _, x, y = P[i]
            xs.add(x)
            ys.add(y)
        ans += len(xs) * len(ys) - len(g)
    print(ans)


if __name__ == "__main__":
    main()
