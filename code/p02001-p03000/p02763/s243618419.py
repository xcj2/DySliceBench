SIZE = 2**20 # 2**20 > N=500000

class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.seg = [0] * (2 * size)

    def update(self, pos, ch):
        # update leaf
        i = self.size + pos - 1
        self.seg[i] = 1 << (ord(ch)-ord('a'))
        # update tree
        while i > 0:
            i = (i - 1) // 2
            self.seg[i] = self.seg[i*2+1] | self.seg[i*2+2]

    def _query(self, a, b, k, left, right):
        if right<a or b<left:
            return 0
        if a<=left and right<=b:
            return self.seg[k]

        vl = self._query(a,b,k*2+1, left, (left+right)//2)
        vr = self._query(a,b,k*2+2, (left+right)//2+1, right)
        return vl | vr

    def query(self, a, b):
        return self._query(a,b,0,0,self.size-1)


def resolve():
    N = int(input())
    S = input().strip()
    Q = int(input())
    table = [[] for _ in range(26)]
    sg = SegmentTree(SIZE)
    for i,ch in enumerate(S):
        sg.update(i, ch)

    for i in range(Q):
        query = input().strip().split()
        if query[0] == '1':
            pos = int(query[1])-1
            sg.update(pos, query[2])
        else:
            left = int(query[1])-1
            right = int(query[2])-1
            bits = sg.query(left, right)
            count = 0
            for j in range(26):
                count += (bits>>j) & 1
            print(count)

resolve()