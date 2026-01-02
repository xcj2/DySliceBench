class SparseTable:
    def __init__(self, a, func=max, one=-10**18):
        self.table = [a[:]]
        self.n = len(a)
        self.logn = self.n.bit_length()
        self.func = func
        self.one = one

        for i in map(lambda x: 1 << x, range(self.logn - 1)):
            self.table.append([])
            for j in range(self.n - i * 2 + 1):
                self.table[-1].append(self.func(self.table[-2][j],
                                                self.table[-2][j + i]))

    def get_section(self, i, j):
        length = j - i
        log = length.bit_length() - 1
        if length <= 0:
            return self.one
        a = self.func(self.table[log][i], self.table[log][j - (1<<log)])
        return a


def low(m, x):
    mi = 0
    ma = m - 1
    if ma < 0 or sp.get_section(0, m) <= x:
        return - 1
    while mi != ma:
        mm = (mi + ma) // 2 + 1
        if sp.get_section(mm, m) > x:
            mi = mm
        else:
            ma = mm - 1
    return mi


def high(m, x):
    mi = m
    ma = n - 1
    if m >= n or sp.get_section(m, n) <= x:
        return n
    while mi != ma:
        mm = (mi + ma) // 2
        if sp.get_section(m, mm+1) > x:
            ma = mm
        else:
            mi = mm + 1
    return mi


n = int(input())
p = [int(i) for i in input().split()]

sp = SparseTable(p)

ans = 0
for i in range(n):
    j = low(i, p[i])
    k = low(j, p[i])
    l = high(i, p[i])
    m = high(l+1, p[i])
    ans += p[i] * ((i-j) * (m-l) + (j-k) * (l-i))
print(ans)
