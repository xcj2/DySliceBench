from bisect import insort, bisect_right, bisect_left


class IntSet:
    def __init__(self) -> None:
        self.total = 0
        self.ms: dict = dict()
        self.lr: list = []

    def insert(self, x: int) -> None:
        if x in self.ms:
            if self.ms[x] == 0:
                self.ms[x] = 1
                self.total += 1
        else:
            self.total += 1
            self.ms[x] = 1
            insort(self.lr, x)
        print(self.total)

    def find(self, x: int) -> None:
        print(self.ms.get(x, 0))

    def delete(self, x: int) -> None:
        if x in self.ms:
            self.total -= self.ms[x]
            self.ms[x] = 0

    def dump(self, l: int, r: int) -> None:
        lb = bisect_left(self.lr, l)
        ub = bisect_right(self.lr, r)
        for i in range(lb, ub):
            k = self.lr[i]
            v = self.ms[k]
            print(f'{k}\n' * v, end='')


if __name__ == "__main__":
    ms = IntSet()
    num_query = int(input())
    for _ in range(num_query):
        op, *v = map(lambda x: int(x), input().split())
        if 0 == op:
            ms.insert(v[0])
        elif 1 == op:
            ms.find(v[0])
        elif 2 == op:
            ms.delete(v[0])
        else:
            ms.dump(v[0], v[1])

