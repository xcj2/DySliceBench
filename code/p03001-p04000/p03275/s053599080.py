from itertools import accumulate

class BIT_RSQ():
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)

    def add(self, i, v):
        while i <= self.n:
            self.data[i-1] += v
            i += i & -i

    def sum(self, i):
        ret = 0
        while(i > 0):
            ret += self.data[i-1]
            i -= i & -i
        return ret

n = int(input())
a = list(map(int, input().split()))

def check(m):
    b = [[-1,1][i>=m] for i in a]
    bit = BIT_RSQ(2*n+1)
    s = [0] + list(accumulate(b))
    res = 0
    for i in range(n):
        bit.add(s[i]+n+1, 1)
        res += bit.sum(s[i+1]+n+1)
    return res >= (n*(n+1)//2+1)//2

left = 0
right = 10**9+1
while right-left > 1:
    mid = (right+left)//2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)