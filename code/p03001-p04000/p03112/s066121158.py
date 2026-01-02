class AvlTree:  # std::set
    def __init__(self, values=None, sorted_=False):
        if values is None:
            self.left = [-1]
            self.right = [-1]
            self.values = [-float("inf")]
            self.diff = [0]  # left - right
            self.size_l = [0]
        else:
            n = len(values)
            self.left = [-1] * (n+1)
            self.right = [-1] * (n+1)
            self.values = [-float("inf")] + values
            self.diff = [0] * (n+1)  # left - right
            self.size_l = [0] * (n+1)
            if not sorted_:
                values.sort()

            st = [[1, n+1, 0]]
            while len(st) > 0:
                l, r, idx_par = st.pop()  # 半開区間
                c = (l+r) >> 1
                if self.values[c] < self.values[idx_par]:
                    self.left[idx_par] = c
                else:
                    self.right[idx_par] = c
                siz = r - l
                if siz & -siz == siz and siz != 1:  # 2冪だったら
                    self.diff[c] = 1
                siz_l = c - l
                self.size_l[c] = siz_l
                if siz_l > 0:
                    st.append([l, c, c])
                    c1 = c + 1
                    if c1 < r:  # 左にノードがなければ右には必ず無いので
                        st.append([c1, r, c])

    # def print(self):
    #     print(f"left  ={self.left}")
    #     print(f"right ={self.right}")
    #     print(f"values={self.values}")
    #     print(f"diff  ={self.diff}")
    #     print(f"dixr_l={self.size_l}")

    def rotate_right(self, idx_par, lr):  # lr: 親の左なら 0
        idx = self.left[idx_par] if lr==0 else self.right[idx_par]
        idx_l = self.left[idx]
        assert idx_l != -1  # 左の子が存在する

        # 部分木の大きさの計算
        self.size_l[idx] -= self.size_l[idx_l] + 1

        # 高さの計算
        a = self.diff[idx]
        b = self.diff[idx_l]  # 左の子の高さの差
        if b >= 0:
            na = a - 1 - b
            if na >= 0:
                nb = b - 1
            else:
                nb = a - 2
        else:
            na = a - 1
            if na >= 0:
                nb = b - 1
            else:
                nb = a + b - 2
        self.diff[idx] = na
        self.diff[idx_l] = nb

        # 回転
        self.left[idx] = self.right[idx_l]
        self.right[idx_l] = idx
        if lr==0:
            self.left[idx_par] = idx_l
        else:
            self.right[idx_par] = idx_l

    def rotate_left(self, idx_par, lr):  # lr: 親の左なら 0
        idx = self.left[idx_par] if lr==0 else self.right[idx_par]
        idx_r = self.right[idx]
        assert idx_r != -1  # 右の子が存在する

        # 部分木の大きさの計算
        self.size_l[idx_r] += self.size_l[idx] + 1

        # 高さの計算
        a = self.diff[idx]
        b = self.diff[idx_r]  # 右の子の高さの差
        if b <= 0:
            na = a + 1 - b
            if na <= 0:
                nb = b + 1
            else:
                nb = a + 2
        else:
            na = a + 1
            if na <= 0:
                nb = b + 1
            else:
                nb = a + b + 2
        self.diff[idx] = na
        self.diff[idx_r] = nb

        # 回転
        self.right[idx] = self.left[idx_r]
        self.left[idx_r] = idx
        if lr == 0:
            self.left[idx_par] = idx_r
        else:
            self.right[idx_par] = idx_r

    def add(self, x):  # insert
        idx = 0
        path = []
        path_left = []
        while idx != -1:
            path.append(idx)
            value = self.values[idx]
            if x == value:
                return  # 重複を許さない
            elif x < value:
                path_left.append(idx)
                idx = self.left[idx]
            else:
                idx = self.right[idx]

        if x < value:
            self.left[path[-1]] = len(self.values)
        else:
            self.right[path[-1]] = len(self.values)
        self.left.append(-1)
        self.right.append(-1)
        self.values.append(x)
        self.diff.append(0)
        self.size_l.append(0)

        for idx_ in path_left:
            self.size_l[idx_] += 1

        idx = path[-1]
        delta_diff = 1 if x < value else -1
        self.diff[idx] += delta_diff
        for idx_par in path[-2::-1]:
            diff = self.diff[idx]
            if diff == 0:
                return
            elif diff == 2:  # 右回転
                idx_l = self.left[idx]  # 左の子
                if self.diff[idx_l] == -1:  # 左右のパターン
                    self.rotate_left(idx, 0)
                self.rotate_right(idx_par, self.right[idx_par]==idx)
                return
            elif diff == -2:  # 左回転
                idx_r = self.right[idx]  # 右の子
                if self.diff[idx_r] == 1:  # 右左のパターン
                    self.rotate_right(idx, 1)
                self.rotate_left(idx_par, self.right[idx_par]==idx)
                return
            else:
                self.diff[idx_par] += 1 if self.left[idx_par]==idx else -1
            idx = idx_par

    def remove(self):  # erase
        raise NotImplementedError

    def __contains__(self, x):  # count
        raise NotImplementedError

    def bisect_left(self, x):  # lower_bound
        idx = self.right[0]
        res = 0
        while idx != -1:
            value = self.values[idx]
            if value == x:
                return res + self.size_l[idx]
            elif value < x:
                res += self.size_l[idx] + 1
                idx = self.right[idx]
            else:
                idx = self.left[idx]
        return res

    def bisect_right(self):  # upper_bound
        raise NotImplementedError


from bisect import bisect_left
import sys
input = sys.stdin.readline
A, B, Q = map(int, input().split())

S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
avl_S = AvlTree(S, True)
avl_T = AvlTree(T, True)

def f(x):
    if 0 <= x and A - 1 >= x:
        return True
    return False
def g(x):
    if 0 <= x and B - 1 >= x:
        return True
    return False

for i in range(Q):
    x = int(input())
    p = avl_S.bisect_left(x)
    m = avl_T.bisect_left(x)

    res = []
    if f(p) and g(m):
        res.append(max(T[m], S[p]) - x)
    if f(p) and g(m - 1):
        res.append(min(S[p] - x, x - T[m - 1]) + S[p] - T[m - 1])
    if f(p - 1) and g(m):
        res.append(T[m] - S[p - 1] + min(T[m] - x, x - S[p - 1]))
    if f(p - 1) and g(m - 1):
        res.append(x - min(T[m - 1], S[p - 1]))
    print(min(res))
