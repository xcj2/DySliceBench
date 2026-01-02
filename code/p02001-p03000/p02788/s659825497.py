import sys
from bisect import bisect_right

sys.setrecursionlimit(500000)


class DualSegmentTree:
    def __init__(self, n) :
        self.n = n
        self.N0 = 1 << n.bit_length()
        self.data = [0] * (self.N0*2)
 
    def update(self, l, r, val) :
        l += self.N0
        r += self.N0
        while l < r:
            if l & 1:
                self.data[l] = self.data[l] + val
                l += 1
            if r & 1:
                self.data[r-1] = self.data[r-1] + val
                r -= 1
            l //= 2
            r //= 2
 
    def query(self, i):
        i += len(self.data) // 2
        ret = self.data[i]
        while i > 0:
            i //= 2
            ret = ret + self.data[i]
        return ret

def main():
    N, D, A = map(int, input().split())
    monsters = []

    for i in range(N):
        x, h = map(int, input().split())
        monsters.append((x,h))

    seg = DualSegmentTree(N)
    monsters.sort()
    X = [0] * N
    H = [0] * N
    for i in range(N):
        X[i], H[i] = monsters[i]
    ans = 0
    for i in range(N):
        tmp_dist = monsters[i][0] + 2 * D
        tmp_hp = int(monsters[i][1] - seg.query(i))
        if tmp_hp <= 0:
            continue
        idx = bisect_right(X, tmp_dist)
        cnt = tmp_hp // A if tmp_hp % A == 0 else tmp_hp // A + 1
        ans += cnt
        seg.update(i,idx,cnt*A)

    print(ans)
    


    


if __name__ == "__main__":
    main()