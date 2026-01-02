
class SegmentTree:
    def __init__(self, base_array,n , default_value = 0, segfunc = lambda a, b: a + b): #元配列、大きさ、デフォルト値
        self._num = 2 ** (n - 1).bit_length()
        self._seg = [default_value] * 2 * self._num
        self._segfunc = segfunc
        self._ide_ele = default_value
        for i in range(n):
            self._seg[i + self._num - 1] = base_array[i]
        for i in range(self._num - 2, -1, -1):
            self._seg[i] = segfunc(self._seg[2 * i + 1], self._seg[2 * i + 2])


    def update(self, k, x):
        k += self._num - 1
        self._seg[k] = x
        while k:
            k = (k - 1) // 2
            self._seg[k] = self._segfunc(self._seg[k * 2 + 1], self._seg[k * 2 + 2])


    def query(self, p, q):
        if q <= p:
            return self._ide_ele
        p += self._num - 1
        q += self._num - 2
        res = self._ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = self._segfunc(res, self._seg[p])
            if q & 1 == 1:
                res = self._segfunc(res, self._seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self._segfunc(res, self._seg[p])
        else:
            res = self._segfunc(self._segfunc(res, self._seg[p]), self._seg[q])
        return res

def main():
    N = int(input())
    S = [c for c in input()]
    M = int(input())

    A = [0 for i in range(N)]

    for i, c in enumerate(S):
        A[i] = 1 << ord(c) - ord('a')

    st = SegmentTree(A, N, 0, lambda a, b: a | b)

    for i in range(M):
        p, a, b = input().split()
        a  = int(a) - 1
        b = int(b) - 1 if p == '2' else b
        if p == '1':
            st.update(a, 1 << ord(b) - ord('a'))

        if p == '2':
            s = st.query(a, b + 1)
            print(bin(s).count('1'))


if __name__ == '__main__':
    main()