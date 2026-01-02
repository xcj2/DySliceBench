class Elements:
    s = set()

    def __init__(self, *elements):
        self.s = set(elements)

    def add(self, x):
        self.s.add(x)

    def remove(self, x):
        self.s.remove(x)

    def union(self, e):
        self.s |= e.s


class Hoge:
    h = {}
    elements_set = set()

    def add(self, at, new_item):
        self.h[at].add(new_item)
        self.h[new_item] = self.h[at]

    def union(self, x, y):
        if len(self.h[y].s) > len(self.h[x].s):
            x, y = y, x

        self.h[x].union(self.h[y])
        self.elements_set.remove(self.h[y])
        for i in self.h[y].s:
            self.h[i] = self.h[x]

    def new_pair(self, x, y):
        u = Elements(x, y)
        self.h[x] = u
        self.h[y] = u
        self.elements_set.add(u)

    def add_pair(self, x, y):
        if x in self.h:
            if y in self.h:
                if self.h[x] is self.h[y]:
                    pass
                else:
                    self.union(x, y)
            else:
                self.add(x, y)
        else:
            if y in self.h:
                self.add(y, x)
            else:
                self.new_pair(x, y)

    def equals(self, *l):
        result = 0

        # 動かさなくても条件を満たすものを数える
        for i, x in enumerate(l):
            if i == x and x not in self.h:
                result += 1

        # 互換の適用によって条件を満たせるものを数える
        for es in self.elements_set:
            s = es.s
            for x in s:
                if l[x] in s:
                    result += 1

        return result


def main():
    n, m = map(int, input().split())
    l = map(lambda s: int(s)-1, input().split())
    hoge = Hoge()
    for i in range(1, m + 1):
       pair = map(lambda s: int(s)-1, input().split())
       hoge.add_pair(*pair)
    print("{0:d}".format(hoge.equals(*l)))


main()
