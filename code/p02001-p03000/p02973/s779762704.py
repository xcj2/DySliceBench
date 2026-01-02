"""
演算子は要素とセットでモノイドを形成するようなものでなければならない。
すなわち、結合律が成り立ち単位元が存在する必要がある。

equalityはsetを高速化するために使う。めんどい場合はNoneにしてもOK
"""
class SegmentTree:

    @classmethod
    def all_identity(cls, operator, equality, identity, size):
        return cls(operator, equality, identity, [identity]*(2 << (size-1).bit_length()))

    @classmethod
    def from_initial_data(cls, operator, equality, identity, data):
        size = 1 << (len(data)-1).bit_length()
        temp = [identity]*(2*size)
        temp[size:size+len(data)] = data
        data = temp

        for i in reversed(range(size)):
            data[i] = operator(data[2*i],data[2*i+1])
        return cls(operator, equality, identity, data)

    # これ使わずファクトリーメソッド使いましょうね
    def __init__(self, operator, equality, identity, data):
        if equality is None:
            equality = lambda a,b: False
        self.op = operator
        self.eq = equality
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
        eq = self.eq
        while i and not eq(data[i],v):
            data[i] = v
            v = op(data[i^1],v) if i & 1 else op(v,data[i^1])
            i >>= 1

    def __iter__(self):
        return self.data[self.size:]

from operator import eq

N = int(input())

B = sorted((v,-i) for i,v in enumerate(int(input()) for _ in range(N)))
B = [-i for v,i in B]
i_j = {j:i for i,j in enumerate(B)}

st = SegmentTree.from_initial_data(min, equality=eq, identity=N, data=B)

visit_cnt = 0
cnt = 0
while visit_cnt < N:
    j = 0
    while True:
        i = st[j:]
        if i == N:
            break
        j = i_j[i]
        visit_cnt += 1
        st[j] = N
    cnt += 1

print(cnt)



