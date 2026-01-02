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
                    self.data[i + (i & -i)] += self.data[i]        

    def point_append(self, index, delta):
        index += 1
        while index < self.n:
            self.data[index] += delta
            index += index & -index
        
    def prefix_folded(self, end):
        res = 0
        while end: # 変更箇所
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

    N, Q = map(int, input().split())
    bit = BIT(list(map(int, input().split())))
    ans = []
    for _ in range(Q):
        a, b, c = map(int, input().split())
        if a:
            ans.append(bit.folded(b, c))
        else:
            bit.point_append(b, c)

    print('\n'.join(map(str, ans)))

if __name__ == "__main__":
    main()