
class SegmentTree:
    """
    演算子は要素とセットでモノイドを形成するようなものでなければならない。
    すなわち、結合律が成り立ち単位元が存在する必要がある。(ただし単位元は添加可能)
    """
    @classmethod
    def all_identity(cls, operator, identity, size):
        return cls(operator, identity, [identity]*(2 << (size-1).bit_length()))

    @classmethod
    def from_initial_data(cls, operator, identity, data):
        size = 1 << (len(data)-1).bit_length()
        temp = [identity]*(2*size)
        temp[size:size+len(data)] = data
        data = temp

        for i in reversed(range(size)):
            data[i] = operator(data[2*i],data[2*i+1])
        return cls(operator, identity, data)

    # これ使わずファクトリーメソッド使いましょうね
    def __init__(self, operator, identity, data):
        self.op = operator
        self.id = identity
        self.data = data
        self.size = len(data)//2

    def _interval(self, a, b):
        a += self.size
        b += self.size
        ra = self.id
        rb = self.id

        data = self.data
        op = self.op
        while a < b:
            if a & 1:
                ra = op(ra,data[a])
                a += 1
            if b & 1:
                b -= 1
                rb = op(data[b],rb)
            a >>= 1
            b >>= 1
        return op(ra,rb)

    def __getitem__(self, i):
        if isinstance(i, slice):
            return self._interval(
                                    0 if i.start is None else i.start,
                                    self.size if i.stop is None else i.stop)
        elif isinstance(i, int):
            return self.data[i+self.size]

    def __setitem__(self, i, v):
        i += self.size
        data = self.data
        op = self.op
        while i:
            data[i] = v
            v = op(data[i^1],v) if i & 1 else op(v,data[i^1])
            i >>= 1

    def __iter__(self):
        return iter(self.data[self.size:])

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

max2 = lambda x,y: x if x > y else y
min2 = lambda x,y: x if x < y else y

L = 300000
N,K = map(int,readline().split())
seg = SegmentTree.all_identity(max2, 0, L+1)

for a in map(int,read().split()):
    seg[a] = seg[max2(0,a-K):min2(L,a+K)+1]+1

print(seg[:])