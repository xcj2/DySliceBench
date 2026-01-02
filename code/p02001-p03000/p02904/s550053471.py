import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
class Min_seg:
    def __init__(self,n,init_val,ide_ele = 10**9):
        # set_val
        self.ide_ele = ide_ele #単位元
        self.n = n #要素数
        self.num = 2 ** (self.n - 1).bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        for i in range(n):
            self.seg[i + self.num - 1] = init_val[i]
            # built
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = min(self.seg[2 * i + 1], self.seg[2 * i + 2])
    def update(self,k, x):
        k += self.num - 1
        self.seg[k] = x
        while k + 1:
            k = (k - 1) // 2
            self.seg[k] = min(self.seg[k * 2 + 1], self.seg[k * 2 + 2])


    def query(self,p, q):
        if q <= p:
            return self.ide_ele
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = min(res, self.seg[p])
            if q & 1 == 1:
                res = min(res, self.seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = min(res, self.seg[p])
        else:
            res = min(min(res, self.seg[p]), self.seg[q])
        return res

class Max_seg:
    def __init__(self,n,init_val,ide_ele = 0):
        # set_val
        self.ide_ele = ide_ele #単位元
        self.n = n #要素数
        self.num = 2 ** (self.n - 1).bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        for i in range(n):
            self.seg[i + self.num - 1] = init_val[i]
            # built
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = max(self.seg[2 * i + 1], self.seg[2 * i + 2])
    def update(self,k, x):
        k += self.num - 1
        self.seg[k] = x
        while k + 1:
            k = (k - 1) // 2
            self.seg[k] = max(self.seg[k * 2 + 1], self.seg[k * 2 + 2])


    def query(self,p, q):
        if q <= p:
            return self.ide_ele
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = max(res, self.seg[p])
            if q & 1 == 1:
                res = max(res, self.seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = max(res, self.seg[p])
        else:
            res = max(max(res, self.seg[p]), self.seg[q])
        return res

n,k = map(int,input().split())
p = list(map(int,input().split()))
seg1 = Min_seg(n,p)
seg2 = Max_seg(n,p)

ans = n-k+1
#print(ans)
for i in range(n-k):
    #print(0,p[i],seg1.query(i,i+k-1))
    #print(1,p[i+k],seg2.query(i+1,i+k+1))
    if p[i] == seg1.query(i,i+k) and p[i+k] == seg2.query(i+1,i+k+1):
        ans -= 1

#print(ans,"試し")

d = [0 for _ in range(n-1)]
for i in range(n-1):
    if p[i] < p[i+1]:
        d[i] = 1

seg3 = Min_seg(n-1,d)
data = [seg3.query(i,i+k-1) for i in range(n-k+1)]
#print(data)


if k > 2 and sum(data) > 1:
    now = -1
    for i in range(n-k+1):
        if data[i] == 1:
            if i == 0:now += 1
            elif data[i-1] == 0:now += 1
    ans -= now

print(ans)