# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
from heapq import heappush, heappop
import sys
from collections import defaultdict
INF = 10**6
def main(H, W, AB):
    cur = list(range(W))
    cur_f = BinaryIndexedTree(initial_values=[1] * W)
    rt = [0] * W
    rt_c = defaultdict(int)
    rt_c[0] = W
    for i, (a, b) in enumerate(AB):
        a -= 1
        mr = -1
        while True:
            j = cur_f.bisect(lambda x: x <= cur_f.query(a - 1))
            if j >= W or j > b: break
            mr = cur[j]
            cur_f.add(j, -1)
            v = j - cur[j]
            if rt_c[v] > 1: rt_c[v] -= 1
            else: rt_c.pop(v)
        if mr >= 0 and b < W:
            cur_f.add(b, 1)
            cur[b] = mr
            v = b - mr
            heappush(rt, v)
            rt_c[v] += 1
        ans = -1
        if rt:
            c = defaultdict(int)
            while rt:
                c[rt[0]] += 1
                if c[rt[0]] > rt_c[rt[0]]:
                    heappop(rt)
                else:
                    ans = rt[0] + i + 1
                    break
        print(ans)

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

    def bisect(self, func):
        '''func()がFalseになるもっとも左のindexを探す
        '''
        n, f, d, v = self.__n, self.__f, self.__d, self.__id
        x, i = 0, 1 << (n.bit_length() - 1)
        while i > 0:
            if x + i <= n and func(f(v, d[x + i])): v, x = f(v, d[x + i]), x + i
            i >>= 1
        return x

if __name__ == '__main__':
    input = sys.stdin.readline
    H, W = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(H)]
    main(H, W, AB)
