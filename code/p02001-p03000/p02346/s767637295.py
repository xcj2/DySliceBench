import math
class segment_tree:
    
    # self.table is 1-indexed
    # math.log2 not implemented 3.2.3
    def __init__(self, dat, query, default=0):
        self.offset = 2 ** math.ceil(math.log(len(dat), 2))
        self.table = [default] * self.offset + dat + [default] * (self.offset - len(dat))
        self.query = query
        for i in reversed(range(1, self.offset)):
            self.table[i] = self.query((self.table[2 * i], self.table[2 * i + 1]))

    # [l, r] closed-interval
    def find(self, l, r):
        return self.query(self.__range(l,r))

    def __range(self, l, r):
        l += self.offset
        r += self.offset
        while l <= r:
            if l & 1:
                yield self.table[l]
                l += 1
            l >>= 1
            if r & 1 == 0:
                yield self.table[r]
                r -= 1
            r >>= 1
        
    def update(self, i, x, function=lambda a, b:b):
        i += self.offset
        self.table[i] = function(self.table[i], x)
        while 1 < i:
            i >>= 1
            self.table[i] = self.query((self.table[2 * i], self.table[2 * i + 1]))

from sys import stdin
readline = stdin.readline


n, q = map(int, readline().split())

rmq = segment_tree([0] * n, sum, default=0)
from operator import add
function = (lambda x, y:rmq.update(x - 1, y, add), lambda x, y:print(rmq.find(x - 1, y - 1)))
for com, x, y in (map(int, readline().split()) for _ in range(q)):
    function[com](x, y)