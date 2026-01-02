# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
from typing import List, Iterable, Tuple
from heapq import heappush, heappop, heapify
import sys
from collections import defaultdict
INF = 10**6
def main(H, W, AB):
    origin = RemovableList(range(W))
    rt = RemovableHeapq([0] * W)
    for i, (a, b) in enumerate(AB):
        a -= 1
        mr = -1
        while True:
            p = origin.get_valid(a)
            if p is None: break
            idx, val = p
            if idx > b: break
            origin.invalidate(idx)
            mr = val
            rt.remove(idx - val)
        if mr >= 0 and b < W:
            origin.validate(b, mr)
            rt.push(b - mr)
        ans = -1
        if not rt.is_empty():
            ans = rt.get_min() + i + 1
        print(ans)

class RemovableList:
    def __init__(self, initial_data: Iterable):
        self.l = list(initial_data)
        self.n = len(self.l)
        self.bit = BinaryIndexedTree(initial_values=[1] * len(self.l))

    def get_valid(self, from_inclusive: int) -> Tuple[int, int]:
        l, bit = self.l, self.bit
        i = bit.bisect(lambda x: x <= bit.query(from_inclusive - 1))
        if i >= self.n:
            return None
        return (i, l[i])

    def invalidate(self, index: int):
        self.bit.add(index, -1)

    def validate(self, index: int, value: int):
        self.bit.add(index, 1)
        self.l[index] = value

    def is_valid(self, index: int) -> bool:
        if index == 0:
            return self.bit.query(0) == 1
        return self.bit.query(index) > self.bit.query(index - 1)

class RemovableHeapq:
    def __init__(self, l: List[int]):
        h = l[:]
        heapify(h)
        d = defaultdict(int)
        for e in l:
            d[e] += 1
        self.h, self.d = l, d

    def push(self, item: int):
        heappush(self.h, item)
        self.d[item] += 1

    def remove(self, item: int) -> bool:
        d = self.d
        if d[item] > 0:
            d[item] -= 1
            return True
        return False

    def get_min(self) -> int:
        h, d = self.h, self.d
        while True:
            m = h[0]
            if d[m] == 0:
                heappop(h)
            else:
                return m

    def is_empty(self) -> bool:
        h, d = self.h, self.d
        while h:
            if d[h[0]] == 0:
                heappop(h)
            else:
                break
        return len(h) == 0

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
