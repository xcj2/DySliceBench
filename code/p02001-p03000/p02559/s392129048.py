class BIT():

    __slots__ = ["n", "data"]

    def __init__(self, length_or_list):
        if isinstance(length_or_list, int):
            self.n = length_or_list + 1
            self.data = [0] * self.n
        else:
            self.n = len(length_or_list) + 1
            self.data = [0] + length_or_list
            for i in range(1, self.n):
                if i + (i & -i) < self.n:
                    self.data[i + (i & -i)] = self.data[i + (i & -i)] + self.data[i]        

    def point_append(self, index, delta):
        index += 1
        while index < self.n:
            self.data[index] = self.data[index] + delta
            index += index & -index
        
    def prefix_folded(self, end):
        res = 0
        while end > 0:
            res += self.data[end]
            end -= end & -end
        return res

    def folded(self, begin, end):
        ret = 0
        while begin < end:
            ret += self.data[end]
            end -= end & -end
        while end < begin:
            ret -= self.data[begin]
            begin -= begin & -begin
        return ret

def main():
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    N, Q = map(int, input().split())
    seg = BIT(list(map(int, input().split())))
    for _ in range(Q):
        a, b, c = map(int, input().split())
        if a:
            print(seg.folded(b, c))
        else:
            seg.point_append(b, c)

if __name__ == "__main__":
    main()