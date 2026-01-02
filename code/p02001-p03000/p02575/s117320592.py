from heapq import *

class erasable_heapq:
    """
    ヒープを二本持って、本来の機能に加えて消去クエリを可能にしたもの。
    存在しない要素を消去しようとすると全体が破綻するので、注意。
    パラメータ:
        data: ヒープに入れる要素のリスト。
        allow_data_destruction: 引数で与えられたリストを破壊してよいかどうか。Trueの方が速い。
    """

    __slots__ = ["data", "to_delete"]

    def __init__(self, data, allow_data_destruction = False):
        if allow_data_destruction:
            self.data = data
        else:
            self.data = data.copy()
        heapify(self.data)
        self.to_delete = []

    def top(self):
        "最小の要素を返す。消去はしない。"
        while self.to_delete and self.to_delete[0] == self.data[0]:
            heappop(self.to_delete)
            heappop(self.data)
        return self.data[0]

    def push(self, elem):
        "ヒープに要素を加える。"
        heappush(self.data, elem)
    
    def pop(self):
        "最小の要素を消去して返す。"
        while self.to_delete and self.to_delete[0] == self.data[0]:
            heappop(self.to_delete)
            heappop(self.data)
        return heappop(self.data)

    def pushpop(self, elem):
        "ヒープにpushし、次にpopを行う、単純なpushとpopの組み合わせより高速な関数。"
        while self.to_delete and self.to_delete[0] == self.data[0]:
            heappop(self.to_delete)
            heappop(self.data)
        return heappushpop(self.data, elem)

    def replace(self ,elem):
        "ヒープにpopし、次にpushを行う、単純なpopとpushの組み合わせより高速な関数。"
        while self.to_delete and self.to_delete[0] == self.data[0]:
            heappop(self.to_delete)
            heappop(self.data)
        return heapreplace(self.data, elem)

    def erase(self, elem):
        """
        ヒープ内の要素を消去する。
        存在しない要素を消去しようとすると全体が破綻するので、注意。
        """
        heappush(self.to_delete, elem)

    def __bool__(self):
        while self.to_delete and self.to_delete[0] == self.data[0]:
            heappop(self.to_delete)
            heappop(self.data)
        return bool(self.data)

    def __len__(self):
        return len(self.data) - len(self.to_delete)


class MultisetBIT:
    """
    最大値が小さい数について、その重複を許した集合を管理する。
    最大値 maxvalue を受け取り、[0, maxvalue] を管理する。
    counter は辞書型かリスト型で、counter[i] が i の個数を持つことを仮定する。
    counter が与えられなかった場合は、全て個数 0 で初期化される。
    閉区間で管理する。
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


H, W = map(int, input().split())

destination = MultisetBIT(W, [1] * W)

destination_to_cost = {i:0 for i in range(W)}

min_heapq = erasable_heapq([0] * W, True)

for k in range(H):
    # print([i for i in range(W) if destination.count(i, i)])
    # print(destination_to_cost)
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    start_point = destination.lower_bound(A)
    point = start_point
    change_dest_flg = False
    while point < W and point < B + 1:
        change_dest_flg = True
        cost = destination_to_cost.pop(point)
        min_heapq.erase(cost)
        if B + 1 != W:
            if (B + 1 in destination_to_cost):
                if destination_to_cost[B+1] > (B + 1 - point) + cost:
                    min_heapq.erase(destination_to_cost[B+1])
                    destination_to_cost[B+1] = (B + 1 - point) + cost
                    min_heapq.push((B + 1 - point) + cost)
            else:
                destination_to_cost[B+1] = (B + 1 - point) + cost
                min_heapq.push((B + 1 - point) + cost)
                destination.add(B+1)
        destination.pop(point)
        point = destination.upper_bound(point)

    if min_heapq:
        print(k + min_heapq.top() + 1)
    else:
        for _ in range(H - k):
            print(-1)
        exit()
