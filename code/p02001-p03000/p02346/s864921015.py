import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, num, ide_ele=0):
        tmp = 1
        while tmp < num:
            tmp *= 2
        self.n = tmp
        self.ide_ele = ide_ele
        self.l = [ide_ele] * (2 * self.n - 1)
    
    def func(self, x, y):
        return x + y
        # return min(x, y)

    def update(self, i, val):
        i = self.n - 1 + i
        self.l[i] += val
        while i > 0:
            i = (i-1)//2
            self.l[i] = self.func(self.l[i*2+1], self.l[i*2+2])
    
    def query(self, a, b, k, l, r):
        # print(a, b, k, l, r)
        if r <= a or b <= l:
            return self.ide_ele
        if a <= l and r <= b:
            return self.l[k]
        vl = self.query(a, b, k*2+1, l, (l+r)//2)
        vr = self.query(a, b, k*2+2, (l+r)//2, r)
        return self.func(vl, vr)

def main():
    N, Q = map(int, input().split())

    segt = SegmentTree(N)

    for _ in range(Q):
        c, x, y = map(int, input().split())
        if c == 0:
            segt.update(x-1, y)
        else:
            print(segt.query(x-1, y, 0, 0, segt.n))
        # print(segt.l)



if __name__ == "__main__":
    main()
