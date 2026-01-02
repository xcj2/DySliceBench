import sys
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class SegmentTree:
    def __init__(self, init_value: list, segfunc, ide_ele):
        n = len(init_value)
        self.N0 = 1 << (n - 1).bit_length()
        self.ide_ele = ide_ele
        self.data = [ide_ele] * (2 * self.N0)
        self.segfunc = segfunc
        
        for i, x in enumerate(init_value):
            self.data[i + self.N0 - 1] = x
        for i in range(self.N0 - 2, -1, -1):
            self.data[i] = self.segfunc(self.data[2 * i + 1], self.data[2 * i + 2])
    
    def update(self, k: int, x):
        k += self.N0 - 1
        ################################################################
        self.data[k] = x
        ################################################################
        while k:
            k = (k - 1) // 2
            self.data[k] = self.segfunc(self.data[k * 2 + 1], self.data[k * 2 + 2])
    
    def query(self, left: int, right: int):
        L = left + self.N0
        R = right + self.N0
        res = self.ide_ele
        ################################################################
        
        while L < R:
            if L & 1:
                res = self.segfunc(res, self.data[L - 1])
                L += 1
            if R & 1:
                R -= 1
                res = self.segfunc(res, self.data[R - 1])
            L >>= 1
            R >>= 1
        
        ################################################################
        return res


def solve():
    N, Q = map(int, rl().split())
    events = []
    xs = set()
    for _ in range(N):
        s, t, x = map(int, rl().split())
        events.append((t - x, 0, x))
        events.append((s - x, 1, x))
        xs.add(x)
    for _ in range(Q):
        d = int(rl())
        events.append((d, 2, -1))
    events.sort(key=itemgetter(0, 1))
    
    x_to_idx = {x: idx for idx, x in enumerate(sorted(xs))}
    M = len(xs)
    ide_ele = 10 ** 10
    seg_tree = SegmentTree([ide_ele] * M, min, ide_ele)
    
    ans = []
    for _, com, pos in events:
        if com == 0:
            seg_tree.update(x_to_idx[pos], ide_ele)
        elif com == 1:
            seg_tree.update(x_to_idx[pos], pos)
        else:
            tmp = seg_tree.data[0]
            ans.append(tmp if tmp != ide_ele else -1)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
