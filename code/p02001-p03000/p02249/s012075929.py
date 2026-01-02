from functools import lru_cache


class MatrixRKSearch:
    shift = 40
    size = 33554393

    def __init__(self, m1, m2):
        self.haystack = self._encode(m1)
        self.needle = self._encode(m2)

    def find(self):
        i1, j1 = len(self.haystack), len(self.haystack[0])
        i2, j2 = len(self.needle), len(self.needle[0])
        if i1 < i2 or j1 < j2:
            return

        hs1 = [self._hash(s, j2) for s in self.haystack]
        hs2 = [self._hash(s, j2) for s in self.needle]
        dm = self.shift**(j2-1) % self.size

        for j in range(j1-j2+1):
            for i in range(i1-i2+1):
                if hs1[i:i+i2] == hs2:
                    yield (i, j)
            if j+j2 < j1:
                for i in range(i1):
                    hs1[i] = self._shift(hs1[i], self.haystack[i][j+j2],
                                         self.haystack[i][j], dm)

    @lru_cache(maxsize=1000)
    def _shift(self, h, add, remove, dm):
        return ((h - remove*dm) * self.shift + add) % self.size

    def _hash(self, s, length):
        h = 0
        for i in range(length):
            h = (h * self.shift + s[i]) % self.size

        return h

    def _encode(cls, m):
        basea = ord('a')
        based = ord('0')
        es = []
        for s in m:
            bs = []
            for c in s:
                if c.isdigit():
                    bs.append(ord(c) - based + 27)
                else:
                    bs.append(ord(c) - basea)
            es.append(bs)

        return es

def run():
    h, w = [int(x) for x in input().split()]
    m = []

    for _ in range(h):
        m.append(input())

    r, c = [int(x) for x in input().split()]
    pt = []

    for _ in range(r):
        pt.append(input())

    sch = MatrixRKSearch(m, pt)
    result = []
    for i, j in sch.find():
        result.append((i, j))

    result.sort()
    for i, j in result:
        print(i, j)


if __name__ == '__main__':
    run()

