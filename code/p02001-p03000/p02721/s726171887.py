# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/SegmentTree.py
class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size : _size + self._len] = data
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


from collections import defaultdict


N, K, C = [int(x) for x in input().split()]
S = input()

# dp[i] stores max number of days worked including day i
dp = SegmentTree([0] * N, 0, max)
for i, x in enumerate(S):
    if x == "o":
        dp[i] = max(1, 1 + dp.query(0, max(0, i - C)))


if any(dp[i] > K for i in range(N)):
    # If it's possible to work more than K days, can always skip any day and still work K
    # No output
    print()
    exit()


#print([dp[i] for i in range(N)])


# Clear out day values that can't reach K
inf = float('inf')
dp2 = SegmentTree([0] * N, inf, min)
for i in range(N - 1, -1, -1):
    days = dp[i]
    if days < K and dp2.query(min(N, i + C + 1), N) != days + 1:
        dp2[i] = inf
    else:
        dp2[i] = days


# Any day values that appear only once is critical
groups = defaultdict(list)
for i in range(N):
    days = dp2[i]
    if days != 0:
        groups[days].append(i)

#print([dp2[i] for i in range(N)])
#print(groups)

mustWork = set()
for k, v in groups.items():
    if len(v) == 1:
        mustWork.update(v)

for i in range(N):
    if i in mustWork:
        print(i + 1)
