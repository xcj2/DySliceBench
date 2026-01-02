import sys

sys.setrecursionlimit(500000)
def input():
    return sys.stdin.readline()[:-1]
class StarrySkyTree:
    # Range Minimum Query
    def __init__(self, N):
        self.LV = (N-1).bit_length()
        self.N0 = 2**self.LV
        self.INF = 2**31 - 1
        self.data = [0]*(2*self.N0)
        self.lazy = [0]*(2*self.N0)

    # 伝搬される区間のインデックス(1-indexed)を全て列挙するgenerator
    def gindex(self, l, r):
        L = l + self.N0; R = r + self.N0
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1; R >>= 1
        while L:
            yield L
            L >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if not v:
                continue
            self.lazy[2*i-1] += v; self.lazy[2*i] += v
            self.data[2*i-1] += v; self.data[2*i] += v
            self.lazy[i-1] = 0

    def update(self, l, r, x):
        # 2. 区間[l, r)のdata, lazyの値を更新
        L = self.N0 + l; R = self.N0 + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] += x; self.data[R-1] += x
            if L & 1:
                self.lazy[L-1] += x; self.data[L-1] += x
                L += 1
            L >>= 1; R >>= 1

        # 3. 更新される区間を部分的に含んだ区間のdataの値を更新 (lazyの値を考慮)
        for i in self.gindex(l, r):
            self.data[i-1] = min(self.data[2*i-1], self.data[2*i]) + self.lazy[i-1]

    def query(self, l, r):
        # 1. トップダウンにlazyの値を伝搬
        self.propagates(*self.gindex(l, r))
        L = self.N0 + l; R = self.N0 + r

        # 2. 区間[l, r)の最小値を求める
        s = self.INF
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R-1])
            if L & 1:
                s = min(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s


def main():
    N,D,A = list(map(int,input().split()))

    enemy = []
    for i in range(N):
        x,h = list(map(int,input().split()))
        if h%A==0:
            enemy.append([x,h//A])
        else:
            enemy.append([x,h//A+1])

    enemy.sort(key=lambda x:x[0])
    def bisect(index):
        x = enemy[index][0]
        if enemy[N-1][0] <= x + 2*D:
            return N-1
        l = index
        r = N-1
        while r-l>1:
            if enemy[(r+l)//2][0] <= x + 2*D:
                l = (r+l)//2
            else:
                r = (r+l)//2
        return l
    ST = StarrySkyTree(N)

    for i in range(N):
        ST.update(i,i+1,enemy[i][1])

    count = 0
    for i in range(N):
        v = ST.query(i,i+1)
        if v>0:
            count += v
            j = bisect(i)
            ST.update(i,j+1,-v) 

    print(count)

if __name__ == '__main__':
    main()

