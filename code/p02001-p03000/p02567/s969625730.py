class RMaxQ:
    
    __slots__ = ["n", "data"]
    
    def __init__(self, li):
        self.n = len(li)
        self.data = li*2
        for i in range(self.n - 1, 0, -1):
            self.data[i] = max(self.data[2*i], self.data[2*i+1])
    
    def get(self, i):
        return self.data[i+self.n]
    
    def update(self, i, a):
        i += self.n
        self.data[i] = a
        while i > 1:
            i //= 2
            self.data[i] = max(self.data[2*i], self.data[2*i+1])
    
    def add(self, i, a):
        i += self.n
        self.data[i] += a
        while i > 1:
            i //= 2
            self.data[i] = max(self.data[2*i], self.data[2*i+1])
    
    def fold(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l < r:
            if l % 2:
                res = max(self.data[l], res)
                l += 1
            if r % 2:
                r -= 1
                res = max(res, self.data[r])
            l //= 2
            r //= 2
        return res
    
    def max_right(self, l, r, check):
        l += self.n
        r += self.n
        left_li = []
        right_li = []
        while l < r:
            if l % 2:
                left_li.append(l)
                l += 1
            if r % 2:
                r -= 1
                right_li.append(r)
            l //= 2
            r //= 2
        temp = 0
        for idx in (left_li + right_li[::-1]):
            if not check(max(temp, self.data[idx])):
                temp = max(temp, self.data[idx])
            else:
                break
        else:
            return -1
        while idx < self.n:
            if check(max(temp, self.data[2*idx])):
                idx = 2*idx
            else:
                temp = max(temp, self.data[2*idx])
                idx = 2*idx+1
        return idx - self.n

import sys
input = sys.stdin.readline
n, q = map(int, input().split())
A = list(map(int, input().split()))
seg = RMaxQ(A)
for _ in range(q):
    t, x, v = map(int, input().split())
    x -= 1
    if t == 1:
        seg.update(x, v)
    elif t == 2:
        print(seg.fold(x, v))
    else:
        ans = seg.max_right(x, n, lambda x: x>=v)
        if ans == -1:
            print(n+1)
        else:
            print(ans+1)