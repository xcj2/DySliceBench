# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, Q, C, LR):
    ans = [0] * Q
    LRi = [(l, r, i) for i, (l, r) in enumerate(LR)]
    LRi.sort(key=lambda x: x[1])
    bit = BinaryIndexedTree(N)
    MR = [-1] * (N + 1)
    p = 0
    for l, r, i in LRi:
        l, r = l - 1, r - 1
        while p <= r:
            c = C[p]
            mr = MR[c]
            if mr >= 0:
                bit.add(mr, -1)
            MR[c] = p
            bit.add(p, 1)
            p += 1
        ans[i] = bit.query(r) - bit.query(l - 1)
    for a in ans:
        print(a)

class BinaryIndexedTree:
    def __init__(self, n=None, f=lambda x, y: x + y, identity=0, initial_values=None):
        assert(n or initial_values)
        self.__f, self.__id, = f, identity
        self.__n = len(initial_values) if initial_values else n
        self.__d = [identity] * (self.__n + 1)
        if initial_values:
            for i, v in enumerate(initial_values): self.add(i, v)

    def add(self, i, v):
        n, f, d = self.__n, self.__f, self.__d
        i += 1
        while i <= n:
            d[i] = f(d[i], v)
            i += -i & i

    def query(self, r):
        res, f, d = self.__id, self.__f, self.__d
        r += 1
        while r:
            res = f(res, d[r])
            r -= -r & r
        return res

if __name__ == '__main__':
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    *C, = map(int, input().split())
    LR = [tuple(map(int, input().split())) for _ in range(Q)]
    main(N, Q, C, LR)
