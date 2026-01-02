
def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

class SegmentTree():
    def __init__(self, n, init_val, segfunc, unifunc):
        self.n = n
        self.size = 2**(n-1).bit_length()
        self.segfunc = segfunc
        self.unifunc = unifunc

        self.seg = [unifunc() for _ in range(2*self.size)]

        for i in range(self.n):
            self.seg[i+self.size-1] = init_val[i]

        for i in range(self.size-2,-1,-1):
            self.seg[i] = self.segfunc(self.seg[2*i+1], self.seg[2*i+2])


    def update(self, k, x):
        k += self.size-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1], self.seg[k*2+2])

    def query(self, p, q): # [p, q)
        if q <= p:
            return self.unifunc()
        p += self.size-1
        q += self.size-2
        res = self.unifunc()

        while q-p > 1:
            if p&1 == 0:
                res = self.segfunc(res, self.seg[p])
            if q&1 == 1:
                res = self.segfunc(res, self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfunc(res, self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
        return res

n = n_in()
S = s_in()
Q = n_in()


dic={i:j for i,j in zip('abcdefghijklmnopqrstuvwxyz',[2**i for i in range(26)])}

T = SegmentTree(n,
    [dic[s] for s in S],
    lambda x,y: x|y,
    lambda: 0
    )

for _ in range(Q):
    n, i, j = input().split()
    if int(n) == 1:
        T.update(int(i)-1, dic[j])
    else:
        print(bin(T.query(int(i)-1, int(j))).count('1'))
