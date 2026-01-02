from heapq import *

class MultisetBIT:
    """
    最大値が小さい数について、その重複を許した集合を管理する。
    最大値 maxvalue を受け取り、[0, maxvalue] を管理する。
    counter は辞書型かリスト型で、counter[i] が i の個数を持つことを仮定する。
    counter が与えられなかった場合は、全て個数 0 で初期化される。
    基本的に閉区間で管理する。
    内部では受け取った数を +1 したものをindexとして持っているので注意。
    """

    __slots__ = ["n", "k", "data"]

    def __init__(self, maxvalue, counter = None):
        self.n = maxvalue + 1
        self.k = 1 << ((self.n + 1).bit_length() - 1)
        self.data = [0] * (self.n + 1)
        if counter is not None:
            self.update(counter)
        
    def update(self, counter):
        """
        counter を受け取って、それを反映させる。
        counter は辞書型かリスト型で、counter[i] が i の個数を持つことを仮定する。
        計算量は、n を要素の最大値として、 O(n) となる。
        """
        if isinstance(counter, list):
            self.data = [0] + counter + [0] * (self.n - len(counter))
        else:
            self.data = [0] * (self.n + 1)
            for k, v in counter.items():
                self.data[k + 1] = v
        for i in range(1, self.n + 1):
            if i + (i & -i) <= self.n:
                self.data[i + (i & -i)] += self.data[i]

    def add(self, value):
        """
        与えられた引数を Multiset に加える。
        計算量は、n を要素の最大値として、 O(log n) となる。
        """
        value += 1
        while value <= self.n:
            self.data[value] += 1
            value += value & -value

    def pop(self, value):
        """
        Multiset から与えられた引数を取り除く。
        与えられた引数が Multiset に入っているかのチェックは行わなず、
        単にその個数を 1 減らすだけなので注意。
        計算量は、n を要素の最大値として、 O(log n) となる。
        """
        value += 1
        while value <= self.n:
            self.data[value] -= 1
            value += value & -value

    def count_le(self, value):
        """
        Multiset 内の要素 elem のうち、0 <= elem <= value を満たすものを数える。
        計算量は、n を要素の最大値として、 O(log n) となる。
        """
        value += 1
        ret = 0
        while value > 0:
            ret += self.data[value]
            value -= value & -value
        return ret

    def count(self, first, last):
        """
        Multiset 内の要素 elem のうち、first <= elem <= last を満たすものを数える。
        計算量は、n を要素の最大値として、 O(log n) となる。
        """
        last += 1
        ret = 0
        while first < last:
            ret += self.data[last]
            last -= last & -last
        while last < first:
            ret -= self.data[first]
            first -= first & -first
        return ret

    def bisect(self, count):
        """
        Multiset 内の要素 elem のうち、count <= count_le(elem) を満たす最小のelemを返す。
        計算量は、n を要素の最大値として、 O(log n) となる。
        """
        ret = 0
        k = self.k
        while k > 0:
            if ret + k <= self.n and self.data[ret + k] < count:
                count -= self.data[ret + k]
                ret += k
            k //= 2
        return ret

    def lower_bound(self, value):
        """
        Multiset 内の要素 elem のうち、value <= elem を満たす最小のelemを返す。
        計算量は、n を要素の最大値として、 O(log n) となる。
        """
        return self.bisect(self.count_le(value - 1) + 1)

    def upper_bound(self, value):
        """
        Multiset 内の要素 elem のうち、value < elem を満たす最小のelemを返す。
        計算量は、n を要素の最大値として、 O(log n) となる。
        """
        return self.bisect(self.count_le(value) + 1)


N, Q = map(int, input().split())
STXs = [tuple(map(int, input().split())) for _ in range(N)]
Ds = [int(input()) for _ in range(Q)]

i2X = sorted(map(lambda t: t[2], STXs))
X2i = {X:i for i, X in enumerate(i2X)}
max_i = len(i2X) - 1
mbit = MultisetBIT(max_i)

events = []
for S, T, X in STXs:
    events.append( ((S - X) << 32) + (X2i[X] << 1)     )
    events.append( ((T - X) << 32) + (X2i[X] << 1) + 1 )
heapify(events)

mask = (1 << 32) - 1
for D in Ds:
    while events:
        if events[0] % 2 == 0:
            if (events[0] >> 32) <= D:
                e = heappop(events)
                mbit.add((e & mask) >> 1)
            else:
                break
        else:
            if (events[0] >> 32) <= D:
                e = heappop(events)
                mbit.pop((e & mask) >> 1)
            else:
                break
    # print([mbit.count(i, i) for i in range(max_i + 1)])
    ans_i = mbit.lower_bound(0)
    print(-1 if ans_i > max_i else i2X[ans_i])