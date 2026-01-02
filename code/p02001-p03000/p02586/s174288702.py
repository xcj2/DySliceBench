import sys

inp = [int(x) for x in sys.stdin.read().split()]; ii = 0

class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

shift = int(10**9 + 1)
rows, cols, k = inp[ii:ii+3]; ii += 3
items = [[] for _ in range(rows+1)]
best = [0]*(cols+1)
for _ in range(k):
	r, c, v = inp[ii:ii+3]; ii += 3
	items[r].append(c*shift+v)
for i in range(rows+1):
	items[i].sort()
S = SegmentTree(best)
ans = 0
for r in range(1, rows+1):
	dp = []
	best1, best2 = 0, 0
	Row = items[r]
	for X in Row:
		c, v = X//shift, X%shift
		v1 = S.query(1, c+1) + v
		v2 = best1 + v
		v3 = best2 + v
		V = v1
		if V < v2:
			V = v2
		if V < v3:
			V = v3
		dp.append(V)
		if v1 > best1:
			best1 = v1
		if v2 > best2:
			best2 = v2
		if ans < V:
			ans = V
	for j in range(len(dp)):
		c = Row[j]//shift
		if S[c] < dp[j]:
			S[c] = dp[j]
print(ans)
