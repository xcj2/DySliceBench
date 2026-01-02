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
        counter は辞書型かリスト型で、counter[i] が i の個数を持つことを仮定する。(0 <= i <= maxvalue)
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
        与えられた引数 value (0 <= value <= maxvalue) を Multiset に加える。
        計算量は、n を要素の最大値として、 O(log n) となる。
        """
        value += 1
        while value <= self.n:
            self.data[value] += 1
            value += value & -value

    def pop(self, value):
        """
        Multiset から与えられた引数 value (0 <= value <= maxvalue) を取り除く。
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
        value は value <= maxvalue を満たす必要がある。
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
        0 <= first <= last <= max_value が必要。
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

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.count(index.start, index.stop - 1)
        else:
            return self.count(index, index)

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
        そのような elem が存在しない場合は maxvalue + 1 を返す。
        計算量は、n を要素の最大値として、 O(log n) となる。
        """
        return self.bisect(self.count_le(value - 1) + 1)

    def upper_bound(self, value):
        """
        Multiset 内の要素 elem のうち、value < elem を満たす最小のelemを返す。
        そのような elem が存在しない場合は maxvalue + 1 を返す。
        計算量は、n を要素の最大値として、 O(log n) となる。
        """
        return self.bisect(self.count_le(value) + 1)

#"""
N = int(input())
S_list = sorted(map(int, input().split()), reverse=True)
"""
N = 18
cs = [1, 18, 153, 816, 3060, 8568, 18564, 31824, 43758, 48620, 43758, 31824, 18564, 8568, 3060, 816, 153, 18, 1]
S_list = []
for i, c in enumerate(cs):
	S_list += [20 - i] * c
#"""

ans_tree = [0] * ((2 ** N) * 2)
ms = MultisetBIT((2 ** N) * 2)
ms.add(1)
prev_S = 0
prev_elem = 0
for S in S_list:
    if prev_S != S:
        prev_elem = 0
    elem = ms.lower_bound(prev_elem)
    while elem != ((2 ** N) * 2 + 1) and ans_tree[elem // 2] == S:
        elem = ms.upper_bound(elem)
    
    if elem == ((2 ** N) * 2 + 1):
        print("No")
        exit()

    prev_S = S
    prev_elem = elem
    ms.pop(elem)
    ans_tree[elem] = S
    elem *= 2
    while elem < 2 ** N * 2:
        ans_tree[elem] = S
        ms.add(elem + 1)
        elem *= 2
    

print("Yes")
# print(ans_tree)
