from collections import UserList


def main():
    _ = input()
    A = Array(input().split(" ")).map(int)
    ans = A.with_index().sort(lambda x: x[1]).map(lambda x: x[0] + 1).join_to_str(" ")
    print(ans)


class Array(UserList):
    def __init__(self, iterable):
        self.data = iterable

    def map(self, f):
        return Array([f(x) for x in self.data])

    def join_to_str(self, sep):
        return sep.join(self.map(str))

    def filter(self, f):
        return Array([x for x in self.data if f(x)])

    def with_index(self):
        return Array([(i, x) for i, x in enumerate(self.data)])

    def sort(self, key):
        return Array(sorted(self.data, key=key))

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def fold_left(self, f, init):
        ret = init
        for x in self.data:
            ret = f(ret, x)
        return ret

    def _scan_left(self, f, init):
        ret = init
        for x in self.data:
            ret = f(ret, x)
            yield ret

    def scan_left(self, f, init):
        return Array(list(self._scan_left(f, init)))

    def lower_bound(self, x):
        """x以上になる最小のindex"""
        low = 0
        high = len(self)
        while low < high:
            mid = (low + high) // 2
            if self[mid] < x:
                low = mid + 1
            else:
                high = mid
        return low

    def upper_bound(self, x):
        """xより大きくなる最小のindex"""
        low = 0
        high = len(self)
        while low < high:
            mid = (low + high) // 2
            if self[mid] <= x:
                low = mid + 1
            else:
                high = mid
        return low

    def _distinct(self):
        dic = {}
        for x in self.data:
            if dic.get(x):
                continue
            dic[x] = True
            yield x

    def distinct(self):
        return Array(list(self._distinct()))


if __name__ == "__main__":
    main()
