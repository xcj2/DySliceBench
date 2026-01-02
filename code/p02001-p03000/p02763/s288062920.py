class my_segment_tree:
    def __init__(self, base_array, size, f=lambda a, b: a + b, default_value = 0):
        self.f = f
        self._seg_size = 2 ** (size.bit_length() + 1) - 1
        self._default_value = default_value
        self._array = [default_value] * (self._seg_size)
        k = 2 ** size.bit_length() - 1  # 一番下の最初のindex

        for i in range(size):
            self._array[k + i] = base_array[i]

        while k > 0:
            for i in range((k + 1) // 2):
                self._array[(k + 2 * i) // 2] = f(self._array[k + 2 * i], self._array[k + 2 * i + 1])
            k //= 2
    def update(self, i, v):
        i += (self._seg_size // 2)
        self._array[i] = v
        while i > 0:
            i = (i - 1) >> 1
            self._array[i] = self.f(self._array[2 * i + 1], self._array[2 * i + 2])

    def get(self, left, right):
        return self._get(left, right, 0, self._seg_size // 2, 0) #どちらも閉空間

    def _get(self, left, right, l, r, i):
        if left <= l and r <= right:
            return self._array[i]

        a = 0
        if left <= (l + r) // 2:
            a = self._get(left, min(right, (l + r) // 2), l, (l + r) // 2, 2 * i + 1)
        b = 0
        if (l + r) // 2 + 1 <= right:
            b= self._get(max(left, (l + r) // 2 + 1), right, (l + r) // 2 + 1, r, 2 * i + 2)

        return self.f(a, b)

def main():
    N = int(input())
    S = input()
    M = int(input())
    A = [0 for i in range(N)]

    for i, c in enumerate(S):
        A[i] = 1 << ord(c) - ord('a')

    st = my_segment_tree(A, N, lambda a, b: a | b)

    for i in range(M):
        p, a, b = input().split()
        a  = int(a) - 1
        if p == '1':
            st.update(a, 1 << (ord(b) - ord('a')))

        if p == '2':
            s = st.get(a, int(b) - 1)
            print(bin(s).count('1'))


if __name__ == '__main__':
    main()