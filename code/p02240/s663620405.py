class QuickUnion:
    def __init__(self, n):
        self.conn = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def union(self, a, b):
        ra = self._root(a)
        rb = self._root(b)

        if ra == rb:
            return

        if self.size[ra] > self.size[rb]:
            self.conn[rb] = ra
            self.size[ra] += self.size[rb]
        else:
            self.conn[ra] = rb
            self.size[rb] += self.size[ra]

    def connected(self, a, b):
        ra = self._root(a)
        rb = self._root(b)

        return ra == rb

    def _root(self, a):
        p = self.conn[a]
        while p != a:
            pp = self.conn[p]
            self.conn[a] = pp
            a, p = p, pp

        return a


def run():
    n, m = [int(i) for i in input().split()]
    u = QuickUnion(n)

    for _ in range(m):
        x, y = [int(i) for i in input().split()]
        u.union(x, y)

    q = int(input())

    for _ in range(q):
        x, y = [int(i) for i in input().split()]
        if u.connected(x, y):
            print('yes')
        else:
            print('no')


if __name__ == '__main__':
    run()

