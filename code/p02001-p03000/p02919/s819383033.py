
from bisect import bisect_left, bisect_right
class OrderedSet:
    def __init__(self, a):
        self.c = {}
        self.a_sort = sorted(list(set(a)))
        for i, a in enumerate(self.a_sort):
            self.c[a] = i + 1
        self.r = {v: k for k, v in self.c.items()}
        self.size = len(self.c)
        self.tree = [0] * (self.size + 1)
        self.num = [0] * self.size
        self.all_count = 0  # 全要素数

    # BITのsum関数
    def _sum(self, index):
        s = 0
        while index:
            s += self.tree[index]
            index -= index & (-index)
        return s

    # xをk個挿入する
    def insert(self, x, k=1):
        index = self.c[x]
        self.num[index - 1] += k
        while index <= self.size:
            self.tree[index] += k
            index += index & (-index)
        self.all_count += k

    # xをk個削除する
    def erase(self, x, k=1):
        self.insert(x, k=-k)

    # 格納しているxの数を返す
    def count(self, x):
        return self.num[self.c[x] - 1]

    # 下から数えてk番目の要素を返す（要素がk個未満のときNoneを返す）
    def get_kth_bottom(self, k):
        if k <= 0:
            return None
        elif self.all_count < k:
            return None
        else:
            i = 0
            s = 0
            step = 1 << (self.size.bit_length() - 1)
            while step:
                if i + step <= self.size and s + self.tree[i + step] < k:
                    i += step
                    s += self.tree[i]
                step >>= 1
            return self.r[i + 1]

    # 上から数えてk番目の要素を返す（要素がk個未満のときNoneを返す）
    def get_kth_top(self, k):
        return self.get_kth_bottom(self.all_count - k + 1)

    # x以上の最小要素を返す
    def lower_bound(self, x):
        p = bisect_left(self.a_sort, x)
        if p == 0:
            k = 1
        else:
            k = self._sum(p) + 1
        return self.get_kth_bottom(k)

    # x以下の最大要素を返す
    def upper_bound(self, x):
        p = bisect_right(self.a_sort, x)
        if p == 0:
            return None
        else:
            k = self._sum(p)
            return self.get_kth_bottom(k)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    P = [0] * (N + 1)
    for i in range(N):
        P[A[i]] = i + 1

    OS = OrderedSet(P)
    ans = 0
    for i in range(N, 0, -1):
        p = P[i]
        c = OS.lower_bound(p)
        d = None if c is None else OS.lower_bound(c + 1)
        b = OS.upper_bound(p)
        a = None if b is None else OS.upper_bound(b - 1)

        a = a if a is not None else 0
        d = d if d is not None else N + 1

        if b is None:
            if c is not None:
                ans += i * p * (d - c)
        elif c is None:
            ans += i * (b - a) * (N - p + 1)
        else:
            ans += i * ((b - a) * (c - p) + (p - b) * (d - c))

        OS.insert(p)

    print(ans)


if __name__ == "__main__":
    resolve()
