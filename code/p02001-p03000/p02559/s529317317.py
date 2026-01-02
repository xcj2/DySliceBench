class BinaryIndexedTree:
    # a[i] = [0] * n
    def __init__(self, n):
        self.size = n
        self.data = [0] * (n+1)

    # return sum(a[0:i])
    def cumulative_sum(self, i):
        ans = 0
        while i > 0:
            ans += self.data[i]
            i -= i & -i
        return ans

    # a[i] += x
    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.data[i] += x
            i += i & -i

def main():
    from sys import stdin
    input = stdin.buffer.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    bit = BinaryIndexedTree(n)
    for i, ai in enumerate(a):
        bit.add(i, ai)

    ans = []
    for _ in range(q):
        typ, i, j = map(int, input().split())
        if typ == 0:
            bit.add(i, j)
        else:
            ans.append(bit.cumulative_sum(j) - bit.cumulative_sum(i))

    for i in ans:
        print(i)

main()