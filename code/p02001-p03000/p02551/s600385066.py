# Modified to do range max updates https://raw.githubusercontent.com/cheran-senthil/PyRival/master/pyrival/data_structures/LazySegmentTree.py
class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the lazy segment tree with data"""
        self._default = default
        self._func = func

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._lazy = [0] * (2 * _size)

        self.data = [default] * (2 * _size)
        self.data[_size : _size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __len__(self):
        return self._len

    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        q, self._lazy[idx] = self._lazy[idx], 0

        self._lazy[2 * idx] = self._func(self._lazy[2 * idx], q)
        self._lazy[2 * idx + 1] = self._func(self._lazy[2 * idx + 1], q)
        self.data[2 * idx] = self._func(self.data[2 * idx], q)
        self.data[2 * idx + 1] = self._func(self.data[2 * idx + 1], q)

    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self.data[idx] = self._func(
                self._func(self.data[2 * idx], self.data[2 * idx + 1]), self._lazy[idx]
            )
            idx >>= 1

    def update(self, start, stop, value):
        """lazily update [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] = self._func(self._lazy[start], value)
                self.data[start] = self._func(self.data[start], value)
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] = self._func(self._lazy[stop], value)
                self.data[stop] = self._func(self.data[stop], value)
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)

    def query(self, start, stop, default=0):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data)


def solve(N, Q, queries):
    N -= 2
    total = N * N
    rows = LazySegmentTree([0] * N, 0, max)
    cols = LazySegmentTree([0] * N, 0, max)
    for t, x in queries:
        assert x >= 2
        x -= 2
        if t == 1:
            c = x
            removed = N - cols.query(c, c + 1)
            assert removed >= 0
            total -= removed
            assert total >= 0
            cols.update(c, c + 1, N)
            rows.update(0, removed, N - c)
        elif t == 2:
            r = x
            removed = N - rows.query(r, r + 1)
            assert removed >= 0
            total -= removed
            assert total >= 0
            rows.update(r, r + 1, N)
            cols.update(0, removed, N - r)
    return total


if False:
    import random

    random.seed(0)
    for _ in range(100):
        print(_)
        N = random.randint(3, 10)
        queries = []
        for i in range(2, N):
            queries.append((1, i))
            queries.append((2, i))

        random.shuffle(queries)
        Q = random.randint(0, min(2 * N - 4, 10))
        queries = queries[:Q]
        print(queries)
        solve(N, len(queries), queries)


N, Q = [int(x) for x in input().split()]
queries = [[int(x) for x in input().split()] for i in range(Q)]

print(solve(N, Q, queries))
