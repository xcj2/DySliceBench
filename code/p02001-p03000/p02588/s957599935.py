import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

class BIT:
    '''
    0-indexed
    '''
    def __init__(self, N):
        self.size = N
        self.tree = [0] * (N + 1)
        self.depth = N.bit_length()

    def _bitsum(self, i):
        ret = 0
        while i:
            ret += self.tree[i]
            i ^= i & -i
        return ret

    def bitsum(self, l, r=None): # [l, r)
        if r is None:
            return self._bitsum(l)
        else:
            return self._bitsum(r) - self._bitsum(l)

    def bitadd(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
        return

    def lower_bound(self, x):
        sum_ = 0
        pos = 0
        v = 1 << self.depth
        for i in range(self.depth, -1, -1):
            k = pos + v
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += v
            v >>= 1
        return pos + 1, sum_


def solve():
    n = ni()
    g = [BIT(20) for _ in range(19)]
    ans = 0
    for _ in range(n):
        a = input().split('.')
        x = int(a[0])*10**9
        if len(a) > 1:
            x += int(a[1] + '0' * (9-len(a[1])))
        t = 0; f = 0
        while x % 2 == 0:
            t += 1
            x //= 2
        while x % 5 == 0:
            f += 1
            x //= 5
        if t > 18: t = 18
        if f > 18: f = 18
        for i in range(18-f, 19):
            ans += g[i].bitsum(18-t, 19)
        g[f].bitadd(t, 1)
    print(ans)
    return

solve()
