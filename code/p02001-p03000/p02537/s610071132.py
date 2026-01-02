def ceil_log2(n):
    i = 0
    while (1 << i) < n:
        i += 1
    return i


class SegmentTree:
    def __init__(self, values, e, op):
        if type(values) == int:
            values = [e] * values

        self._n = len(values)
        self._ceil_log2_n = ceil_log2(self._n)
        self._size = 1 << self._ceil_log2_n

        self._e = e

        self._op = op

        self._nodes = [e] * (2 * self._size)
        for i, value in enumerate(values):
            self._nodes[self._size + i] = value

        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, index, value):
        self._nodes[self._size + index] = value
        for i in range(1, self._ceil_log2_n + 1):
            self._update((self._size + index) >> i)

    def get(self, index):
        return self._nodes[self._size + index]

    def all_prod(self):
        return self._nodes[1]

    def prod(self, left, right):
        if left == right:
            return self._e

        if left == 0 and right == self._n:
            return self.all_prod()

        left_prod = self._e
        right_prod = self._e

        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                left_prod = self._op(left_prod, self._nodes[left])
                left += 1

            if right & 1:
                right -= 1
                right_prod = self._op(self._nodes[right], right_prod)

            left >>= 1
            right >>= 1

        return self._op(left_prod, right_prod)

    def _update(self, index):
        self._nodes[index] = self._op(self._nodes[2 * index], self._nodes[2 * index + 1])


def main():
    n, k = map(int, input().split())
    arr = [int(input()) for _ in range(n)]

    overall_max_len = 0
    seg = SegmentTree(3 * 10 ** 5 + 1, 0, max)

    for value in arr:
        max_len = seg.prod(max(0, value - k), min(3 * 10 ** 5 + 1, value + k + 1)) + 1
        seg.set(value, max_len)
        overall_max_len = max(overall_max_len, max_len)

    print(overall_max_len)


main()
