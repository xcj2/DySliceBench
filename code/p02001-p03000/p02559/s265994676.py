class BIT():

    __slots__ = ["func", "e", "n", "data"]

    def __init__(self, length_or_list, func, e):
        self.func = func
        self.e = e
        if isinstance(length_or_list, int):
            self.n = length_or_list + 1
            self.data = [self.e] * self.n
        else:
            self.n = len(length_or_list) + 1
            self.data = [self.e] + length_or_list
            for i in range(1, self.n):
                if i + (i & -i) < self.n:
                    self.data[i + (i & -i)] = self.func(self.data[i + (i & -i)], self.data[i])        

    def point_append(self, index, delta):
        index += 1
        while index < self.n:
            self.data[index] = self.func(self.data[index], delta)
            index += index & -index
        
    def prefix_folded(self, end):
        res = 0
        while end > 0:
            res = self.func(res, self.data[end])
            end -= end & -end
        return res

def main():
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    N, Q = map(int, input().split())
    seg = BIT(list(map(int, input().split())), lambda a, b: a + b, 0)
    for _ in range(Q):
        a, b, c = map(int, input().split())
        if a:
            print(seg.prefix_folded(c) - seg.prefix_folded(b))
        else:
            seg.point_append(b, c)

if __name__ == "__main__":
    main()