class BIT():

    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        '''i番目の要素にxを加算する'''
        i = i + 1
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def get(self, i, j):
        '''[i, j)の和を求める'''
        return self._sum(j) - self._sum(i)


n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

cumsum_a = [0]*(n+1)
for i in range(n):
    cumsum_a[i+1] = cumsum_a[i] + a[i]
for i in range(n+1):
    cumsum_a[i] = cumsum_a[i] - k*i

#座標圧縮したリストを返す
def compress(list1):
    len_list1 = len(list1)
    list11 = sorted(set(list1))
    memo = {value : index for index, value in enumerate(list11)}
    list2 = [0]*(len_list1)
    for i in range(len_list1):
        list2[i] = memo[list1[i]]
    return list2

cumsum_a = compress(cumsum_a)

bit = BIT(n+1)
ans = 0
for i in range(n+1):
    ans += bit.get(0, cumsum_a[i] + 1)
    bit.add(cumsum_a[i], 1)
print(ans)