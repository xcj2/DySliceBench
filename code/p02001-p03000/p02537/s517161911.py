from sys import stdin
read = stdin.read
readline = stdin.readline
def i_input(): return int(readline().rstrip())
def i_map(): return map(int, readline().rstrip().split())
def i_list(): return list(i_map())

MAX_A = 300005

class SegmentTree:
    def __init__(self, n:int, p:list, ide_ele, func):
        self.num = 1 << ((n-1).bit_length())
        self.tree = [ide_ele]*(2*self.num)
        for i in range(n):
            self.tree[i+self.num] = p[i]
        for i in range(self.num-1, 0, -1):
            self.tree[i] = func(self.tree[i << 1], self.tree[(i << 1)+1])
        self.f = func
        self.ide_ele = ide_ele

    def update(self, i, x):
        i += self.num
        self.tree[i] = x
        while i:
            i >>= 1
            self.tree[i] = self.f(self.tree[i << 1], self.tree[(i << 1)+1])

    def query(self, l, r):
        ansl = ansr = self.ide_ele
        l += self.num
        r += self.num-1
        if l == r:
            return self.tree[l]
        while l < r:
            if l & 1:
                ansl = self.f(ansl, self.tree[l])
                l += 1
            if ~r & 1:
                ansr = self.f(self.tree[r], ansr)
                r -= 1
            l >>= 1
            r >>= 1
        if l == r:
            ansl = self.f(ansl, self.tree[l])
        return self.f(ansl, ansr)

def main():
    N, K = i_map()
    A = list(map(int, read().strip().splitlines()))
    s = SegmentTree(MAX_A, [0]*MAX_A, 0, lambda x, y : max(x,y))
    ans = 0
    for a in A:
        l, r = max(a - K, 0), min(a + K + 1, MAX_A)
        now = s.query(l, r) + 1
        s.update(a, now)
        ans = max(ans, now)
    print(ans)

if __name__ == "__main__":
    main()
