class SegTreeBool():
    def segFunc(self, x, y):
        return x + y
    def searchIndexFunc(self, val):
        return val > 0
    def __init__(self, ide, init_val):
        n = len(init_val)
        self.ide_ele = ide
        self.num = 2**(n-1).bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        for i in range(n):
            self.seg[i+self.num-1] = init_val[i]    
        for i in range(self.num-2,-1,-1):
            self.seg[i] = self.segFunc(self.seg[2*i+1],self.seg[2*i+2])
    def update(self, idx, val):
        idx += self.num-1
        self.seg[idx] = val
        while idx:
            idx = (idx-1)//2
            self.seg[idx] = self.segFunc(self.seg[idx*2+1], self.seg[idx*2+2])
    def query(self, begin, end):
        if end <= begin:
            return self.ide_ele
        begin += self.num-1
        end += self.num-2
        res = self.ide_ele
        while begin + 1 < end:
            if begin&1 == 0:
                res = self.segFunc(res, self.seg[begin])
            if end&1 == 1:
                res = self.segFunc(res, self.seg[end])
                end -= 1
            begin = begin//2
            end = (end-1)//2
        if begin == end:
            res = self.segFunc(res, self.seg[begin])
        else:
            res = self.segFunc(self.segFunc(res, self.seg[begin]), self.seg[end])
        return res
    def getLargestIndex(self, begin, end):
        L, R = begin, end
        if not self.searchIndexFunc(self.query(begin, end)):
            return None
        while L+1 < R:
            P = (L+R)//2
            if self.searchIndexFunc(self.query(P, R)):
                L = P
            else:
                R = P
        return L
    def getSmallestIndex(self, begin, end):
        L, R = begin, end
        if not self.searchIndexFunc(self.query(begin, end)):
            return None
        while L+1 < R:
            P = (L+R+1)//2
            if self.searchIndexFunc(self.query(L, P)):
                R = P
            else:
                L = P
        return L

def main():
    n, q = map(int, input().split())
    qry = [list(map(int, input().split())) for _ in range(q)]
    ans = (n-2)**2
    m1, m2 = n, n
    segbool1 = SegTreeBool(0, [0]*n)
    segbool2 = SegTreeBool(0, [0]*n)
    ms1 = [n]*n
    ms2 = [n]*n
    for ptn, idx in qry:
        if ptn == 1:
            tmp = None
            if segbool1.query(0, idx) == 0:
                tmp = m2 - 2
            else:
                pt = segbool1.getLargestIndex(0, idx)
                tmp = ms1[pt]
            ans -= tmp
            ms1[idx] = tmp
            segbool1.update(idx, 1)
            if idx < m1:
                m1 = idx
        else:
            tmp = None
            if segbool2.query(0, idx) == 0:
                tmp = m1 - 2
            else:
                pt = segbool2.getLargestIndex(0, idx)
                tmp = ms2[pt]
            ans -= tmp
            ms2[idx] = tmp
            segbool2.update(idx, 1)
            if idx < m2:
                m2 = idx
    print(ans)

if __name__ == "__main__":
    main()