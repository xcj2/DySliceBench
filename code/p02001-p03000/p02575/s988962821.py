from heapq import *
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

class BitSum:
    def __init__(self, n):
        self.n = n + 1
        self.table = [0] * self.n

    def add(self, i, x):
        i += 1
        while i < self.n:
            self.table[i] += x
            i += i & -i

    def sum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.table[i]
            i -= i & -i
        return res

    # 数列を度数分布とみたときに、x番目がどのインデックスにあるかを返す
    def rank(self, x):
        idx = 0
        for lv in range((self.n - 1).bit_length() - 1, -1, -1):
            mid = idx + (1 << lv)
            if mid >= self.n: continue
            if self.table[mid] < x:
                x -= self.table[mid]
                idx += 1 << lv
        return idx

def solve():
    bit = BitSum(w + 1)
    for j in range(w): bit.add(j + 1, 1)
    cost = [0] * (w + 1)
    hp = [0] * w
    heapify(hp)
    rem = []

    for i in range(h):
        l, r = MI()
        r += 1
        # cost[r]の更新
        if r <= w:
            cnt = bit.sum(r)
            if cnt:
                j = bit.rank(cnt)
                if l <= j < r:
                    bit.add(r, 1)
                    cost[r] = cost[j] + r - j
                    heappush(hp, cost[r])
        # 区間[l,r)を無効にする
        cnt = bit.sum(l - 1)
        while 1:
            j = bit.rank(cnt + 1)
            if j >= r: break
            heappush(rem, cost[j])
            bit.add(j, -1)
        # ヒープからの削除
        while hp and rem and hp[0] == rem[0]:
            heappop(hp)
            heappop(rem)
        # 出力
        if hp: print(hp[0] + i + 1)
        else: print(-1)

h,w=MI()
solve()
