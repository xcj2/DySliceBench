from operator import itemgetter


class UnionFindTree():
    def __init__(self, N):
        self.__parent_of = [None] * N
        self.__rank_of = [0] * N
        self.__size = [1] * N

    def __root(self, value):
        if self.__parent_of[value] is None:
            return value
        else:
            self.__parent_of[value] = self.__root(self.__parent_of[value])
            return self.__parent_of[value]

    def unite(self, a, b):
        r1 = self.__root(a)
        r2 = self.__root(b)
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
        return self.__root(a) == self.__root(b)

    def size(self, a):
        return self.__size[self.__root(a)]

    def groups(self):
        groups = {}
        for k in self.__parent_of.keys():
            r = self.__root(k)
            if r not in groups:
                groups[r] = []
            groups[r].append(k)
        return [groups[x] for x in groups]


def main():
    N = int(input())
    X = [None] * N
    Y = [None] * N
    for i in range(N):
        x, y = map(int, input().split())
        X[i] = (x, i)
        Y[i] = (y, i)
    X.sort(key=itemgetter(0))
    Y.sort(key=itemgetter(0))
    adj = [None] * (2*N - 2)
    for i in range(N-1):
        adj[2*i] = (X[i+1][0] - X[i][0], X[i][1], X[i+1][1])
        adj[2*i+1] = (Y[i+1][0] - Y[i][0], Y[i][1], Y[i+1][1])
    adj.sort(key=itemgetter(0))
    uft = UnionFindTree(N)
    ans = 0
    for pair in adj:
        cost, a, b = pair
        if not uft.is_same(a, b):
            uft.unite(a, b)
            ans += cost
        if uft.size(a) == N:
            break
    print(ans)


if __name__ == "__main__":
    main()
