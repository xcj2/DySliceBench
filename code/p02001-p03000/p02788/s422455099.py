import sys,bisect
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main():
    # 区間加算、上書き、一点取得
    class SegmentTree:
        def __init__(self, n, ele, segfun):
            #####単位元######要設定0or1orinf
            self.ide_ele = ele
            self.segfun = segfun
            ####################
            self.n = n
            self.N0 = 1 << n.bit_length()
            self.data = [self.ide_ele] * (self.N0 * 2)
 
        def update_add(self, l, r, val):
            l += self.N0
            r += self.N0
            while l < r:
                if l & 1:
                    self.data[l] += val
                    l += 1
                if r & 1:
                    self.data[r - 1] += val
                    r -= 1
                l //= 2
                r //= 2
 
        def update(self, l, r, val):
            l += self.N0
            r += self.N0
            while l < r:
                if l & 1:
                    self.data[l] = self.segfun(self.data[l], val)
                    l += 1
                if r & 1:
                    self.data[r - 1] = self.segfun(self.data[r - 1], val)
                    r -= 1
                l //= 2
                r //= 2
 
        def query(self, i):
            i += len(self.data) // 2
            ret = self.data[i]
            while i > 0:
                i //= 2
                ret = self.segfun(ret, self.data[i])
            return ret
 
    N, D, A = map(int,readline().split())
    X = [list(map(int,readline().split())) for _ in range(N)]
    X.sort()
    L = [0]*N
    for i in range(N):
        L[i] = X[i][0]
    S = SegmentTree(N,0,lambda a, b: a+b)
    ans = 0
    for i,[x,h] in enumerate(X):
        H = h - S.query(i)
        if H<=0:
            continue
        ind = bisect.bisect(L,x+2*D)
        need = (H-1)//A + 1
        S.update(i,ind,need*A)
        ans += need
    print(ans)
    return

if __name__ == '__main__':
    main()