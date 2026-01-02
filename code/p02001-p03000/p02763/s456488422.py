from operator import add, mul, sub, or_


class SegmentTree:
    '''
    1-indexd セグメント木
    values : 値の配列
    op : 区間に対する関数
    ie : 初期値
    '''

    def __init__(self, values, op, ie):
        self.values = values
        vlen = len(values)
        self.op = op
        self.size = 2 ** (vlen-1).bit_length()
        self.tree = [ie]*self.size + self.values + [ie]*(self.size-vlen)
        self.ie = ie

        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.op(self.tree[i*2], self.tree[i*2+1])

    def update(self, i, v):
        i += self.size
        self.tree[i] = v
        while i > 0:
            i //= 2
            self.tree[i] = self.op(self.tree[i*2], self.tree[i*2+1])

    def query(self, l, r):
        l += self.size
        r += self.size
        ret = self.ie
        while l < r:
            if l & 1:
                ret = self.op(ret, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ret = self.op(ret, self.tree[r])
            l //= 2
            r //= 2
        return ret


def bit(c):
    return 1 << (ord(c)-ord('a'))


def bitcount(c):
    b = bin(c)[2:]
    return b.count("1")


N = int(input())
s = input().strip()
Q = int(input())

seg = SegmentTree([bit(c) for c in s], or_, 0)
for q in range(Q):
    i, l, r = input().split()
    if i == "1":
        l = int(l)-1
        seg.update(l, bit(r))
    else:
        l = int(l)-1
        r = int(r)-1
        v = seg.query(l, r+1)
        print(bitcount(v))
