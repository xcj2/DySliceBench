from sys import stdin
input = stdin.readline

class SegTreeFlag():
    def segFunc(self, x, y):
        return x+y
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

class SegTreeMin():
    def segFunc(self, x, y):
        if x < y:
            return x
        else:
            return y
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

h, w = map(int, input().split())
wall = [list(map(int, input().split())) for _ in range(h)]
ans = [-1 for _ in range(h)]
segflag = SegTreeFlag(0, [1 for _ in range(w+2)])
segmin = SegTreeMin(10**9, [0 for _ in range(w+2)])
segmin.update(0, 10**9)
for i in range(h):
    idx = segflag.getLargestIndex(0, wall[i][1]+2)
    if idx < wall[i][1]+1:
        segflag.update(wall[i][1]+1, 1)
        segmin.update(wall[i][1]+1, segmin.query(idx, idx+1)+(wall[i][1]+1-idx))
    cnt = segflag.query(wall[i][0], wall[i][1]+1)
    for _ in range(cnt):
        idx = segflag.getSmallestIndex(wall[i][0], wall[i][1]+1)
        segflag.update(idx, 0)
        segmin.update(idx, 10**9)
    tmp = segmin.query(0, w+1)
    if tmp < 10**9:
        ans[i] = tmp + i + 1
    else:
        break
for v in ans:
    print(v)