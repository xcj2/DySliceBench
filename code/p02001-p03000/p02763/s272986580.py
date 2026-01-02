from collections import namedtuple


def _hasParents(i):
    return i > 1


def _isLeftChild(i):
    return i % 2 == 0


def _isRightChild(i):
    return i % 2 == 1


def _parentNode(i):
    return i // 2


def _leftChild(i):
    return 2 * i


def _rightChild(i):
    return 2 * i + 1


def _leftSibling(i):
    return i - 1


def _rightSibling(i):
    return i + 1


def _nextPowerOfTwo(n):
    ret = 1
    while ret < n:
        ret *= 2
    return ret


def ancestors(i):
    while _hasParents(i):
        i = _parentNode(i)
        yield i


Config = namedtuple("Config", ["mconvert", "mappend", "mempty"])


class SegmentTree:
    def __init__(self, arr, mconvert, mappend, mempty, minCapacity=1):
        def wrappedMconvert(x):
            if x is not None:
                return mconvert(x)
            else:
                return mempty()

        def wrappedMappend(x, y):
            xEmpty = x == mempty()
            if xEmpty:
                return y
            yEmpty = y == mempty()
            if yEmpty:
                return x
            if xEmpty and yEmpty:
                return mempty()
            return mappend(x, y)

        self.config = Config(
            mconvert=wrappedMconvert, mappend=wrappedMappend, mempty=mempty
        )

        # Init empty tree
        self.MAX_SIZE = _nextPowerOfTwo(max(len(arr), minCapacity))
        self.values = [None] * self.MAX_SIZE
        self.accumulations = [self.config.mempty()] * (2 * self.MAX_SIZE)
        self.numValues = 0

        # Init values
        self.values[: len(arr)] = arr
        self.numValues = len(arr)
        # Init leaf accumulations
        self.accumulations[self.MAX_SIZE : self.MAX_SIZE + len(arr)] = map(
            self.config.mconvert, arr
        )
        # Init parent accumulations
        for parent in range(self.MAX_SIZE - 1, -1, -1):
            self.accumulations[parent] = self.config.mappend(
                self.accumulations[_leftChild(parent)],
                self.accumulations[_rightChild(parent)],
            )

    def query(self, i, j):
        # Inclusive i, exclusive j
        if not (0 <= i <= j <= self.numValues):
            raise IndexError
        if i == j:
            return self.config.mempty()
        leftTotal = self.config.mempty()
        rightTotal = self.config.mempty()
        l = self.MAX_SIZE + i
        r = self.MAX_SIZE + j - 1  # make inclusive both endpoints for calculations
        while l <= r:
            if _isRightChild(l):
                leftTotal = self.config.mappend(leftTotal, self.accumulations[l])
                l = _rightSibling(l)
            l = _parentNode(l)

            if _isLeftChild(r):
                rightTotal = self.config.mappend(self.accumulations[r], rightTotal)
                r = _leftSibling(r)
            r = _parentNode(r)
        return self.config.mappend(leftTotal, rightTotal)

    def append(self, x):
        assert self.numValues + 1 <= self.MAX_SIZE
        self.numValues += 1
        self.__setitem__(self.numValues - 1, x)

    def pop(self, i=None):
        if i is not None:
            raise NotImplementedError
        if not self.numValues:
            raise IndexError
        ret = self.__getitem__(self.numValues - 1)
        self.__delitem__(self.numValues - 1)
        return ret

    def insert(self, i, x):
        raise NotImplementedError

    def __getitem__(self, index):
        if isinstance(index, slice):
            raise NotImplementedError
        if not 0 <= index < self.numValues:
            raise IndexError
        ret = self.values[index]
        assert ret is not None
        return ret

    def __setitem__(self, i, x):
        if isinstance(i, slice):
            raise NotImplementedError

        if not 0 <= i < self.numValues:
            raise IndexError
        index = self.MAX_SIZE + i
        self.values[i] = x
        self.accumulations[index] = self.config.mconvert(x)
        for parent in ancestors(index):
            self.accumulations[parent] = self.config.mappend(
                self.accumulations[_leftChild(parent)],
                self.accumulations[_rightChild(parent)],
            )
            parent = _parentNode(parent)

    def __delitem__(self, i):
        if isinstance(i, slice):
            raise NotImplementedError
        if not 0 <= i < self.numValues:
            raise IndexError
        index = self.MAX_SIZE + i
        self.values[i] = None
        self.accumulations[index] = self.config.mempty()
        for parent in ancestors(index):
            self.accumulations[parent] = self.config.mappend(
                self.accumulations[_leftChild(parent)],
                self.accumulations[_rightChild(parent)],
            )
        self.numValues -= 1

    def __len__(self):
        return self.numValues


def charToBitmask(c):
    return 1 << (ord(c) - ord("a"))


def popcount(i):
    # Python doesn't have __builtin_popcount
    # https://stackoverflow.com/a/407758
    assert 0 <= i < 0x100000000
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xFFFFFFFF) >> 24


N, = list(map(int, input().split()))
S = input()
Q, = list(map(int, input().split()))
queries = []
for i in range(Q):
    queries.append(input().split())


segTree = SegmentTree(S, charToBitmask, lambda mask1, mask2: mask1 | mask2, lambda: 0)
out = []
for query in queries:
    if query[0] == "1":
        _, i, c = query
        i = int(i) - 1
        segTree[i] = c
    elif query[0] == "2":
        _, l, r = query
        l = int(l) - 1
        r = int(r) - 1
        mask = segTree.query(l, r + 1)
        out.append(str(popcount(mask)))
print("\n".join(out))

