def euler_tour(tree: list, root: int):
    """オイラーツアーを行う"""
    n = len(tree)
    par = {root: -1}
    trail = []
    is_up = []
    stack = [root]
    while stack:
        v = stack.pop()
        if v >= 0:  # 行きがけ順の処理
            trail.append(v)
            is_up.append(0)
            stack.append(~v)
            for nxt_v in tree[v]:
                if nxt_v not in par:
                    par[nxt_v] = v
                    stack.append(nxt_v)
                    

        else:  # 帰りがけ順の処理
            if ~v == root:
                continue
            trail.append(par[~v])
            is_up.append(1)
 
    return trail, is_up


class BIT:
    """区間加算、一点取得クエリをそれぞれO(logN)で答えるデータ構造"""
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (n + 1)

    def build(self, array):
        """arrayを初期値とするBinaryIndexTreeを構築する O(N)"""
        for i in range(1, self.size + 1):
            if i - 1 + (i & -i) >= self.size:
                self.bit[i] = array[i - 1]
            else:
                self.bit[i] = array[i - 1] - array[i + (i & -i) - 1]

    def _add(self, i, val):
        while i > 0:
            self.bit[i] += val
            i -= i & -i

    def get_val(self, i):
        """i番目の値を求める"""
        i = i + 1
        s = 0
        while i <= self.size:
            s += self.bit[i]
            i += i & -i
        return s

    def add(self, l, r, val):
        """区間[l, r)にvalを加える"""
        self._add(r, val)
        self._add(l, -val)


from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
c = list(map(int, input().split()))
info = [list(map(int, input().split())) for i in range(n - 1)]

tree = [[] for i in range(n)]
for a, b in info:
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

# 葉に対する頂点と辺の追加
plus = n + 1
for i in range(1, n):
   if len(tree[i]) == 1:
        info.append([i + 1, plus])
        plus += 1
# 根に対する頂点と辺の追加
info.append([1, plus])

new_n = len(info) + 1
tree = [[] for i in range(new_n)]
for a, b in info:
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

root = new_n - 1
et, is_up = euler_tour(tree, root)

bit = BIT(n)
stack = [[] for i in range(n)]
ans = [0] * n

for i in range(len(et)):
    if et[i] >= n:
        continue

    if is_up[i]:
        ind = i
        i = c[et[i]] - 1
        val = bit.get_val(i)
        ans[i] += val * (val + 1) // 2

        bit.add(i, i + 1, -val)
        if len(stack[i]) >= 1 and is_up[ind + 1]:                                                               
            tmp = stack[i].pop()                                                             
            bit.add(i, i + 1, tmp)    
    else:
        i = c[et[i]] - 1
        val = bit.get_val(i)
        stack[i].append(val)
        bit.add(0, n, 1)
        bit.add(i, i + 1, -(val + 1))

for i in range(n):
    val = bit.get_val(i)
    ans[i] += val * (val + 1) // 2

for i in range(n):
    print(n * (n + 1) // 2 - ans[i])