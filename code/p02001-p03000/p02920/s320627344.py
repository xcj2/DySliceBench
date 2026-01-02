from bisect import bisect_left

class SegTree():
    def segfunc(self, x, y):
        return x+y

    def __init__(self, ide, init_val):
        n = len(init_val)
        self.ide_ele = ide
        self.num = 2**(n-1).bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        for i in range(n):
            self.seg[i+self.num-1] = init_val[i]    
        for i in range(self.num-2,-1,-1):
            self.seg[i] = self.segfunc(self.seg[2*i+1],self.seg[2*i+2]) 
    def update(self, idx, val):
        idx += self.num-1
        self.seg[idx] = val
        while idx:
            idx = (idx-1)//2
            self.seg[idx] = self.segfunc(self.seg[idx*2+1], self.seg[idx*2+2])
    def query(self, begin, end):
        if end <= begin:
            return self.ide_ele
        begin += self.num-1
        end += self.num-2
        res = self.ide_ele
        while begin + 1 < end:
            if begin&1 == 0:
                res = self.segfunc(res, self.seg[begin])
            if end&1 == 1:
                res = self.segfunc(res, self.seg[end])
                end -= 1
            begin = begin//2
            end = (end-1)//2
        if begin == end:
            res = self.segfunc(res, self.seg[begin])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[begin]), self.seg[end])
        return res

def main():
    lim = int(input())
    s = list(map(int, input().split()))
    n = len(s)
    s.sort()
    f = True
    tmp = [1]*n
    tmp[n-1] = 0
    seg = SegTree(0, tmp)
    st = set()
    st.add(n-1)
    for _ in range(1, lim+1):
        adst = set()
        for v in st:
            u = bisect_left(s, s[v])
            if seg.query(0, u) == 0:
                f = False
                break
            L, R = 0, u
            while L+1 < R:
                P = (L+R)//2
                if seg.query(P, u) > 0:
                    L = P
                else:
                    R = P
            seg.update(L, 0)
            adst.add(L)
        for v in adst:
            st.add(v)
    if f:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()