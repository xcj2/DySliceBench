class BIT():
    """区間加算、一点取得クエリをそれぞれO(logN)で答える
    add: 区間[l, r)にvalを加える
    get_val: i番目の値を求める
    i, l, rは0-indexed
    """
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def _add(self, i, val):
        while i > 0:
            self.bit[i] += val
            i -= i & -i

    def get_val(self, i):
        """i番目の値を求める"""
        i = i + 1
        s = 0
        while i <= self.n:
            s += self.bit[i]
            i += i & -i
        return s

    def add(self, l, r, val):
        """区間[l, r)にvalを加える"""
        self._add(r, val)
        self._add(l, -val)


from operator import itemgetter
n, d, a = map(int, input().split())
info = [list(map(int, input().split())) for i in range(n)]

info = sorted(info, key = itemgetter(0))
bit = BIT(n)

for i in range(n):
    bit.add(i, i+1, info[i][1])

info.append([10**18, 0])
ans = 0 
r = 0
for i in range(n):
    num = bit.get_val(i)
    if num <= 0:
        continue
    while True:
        if info[r][0] - info[i][0] > 2*d:
            break
        else:
            r += 1
    ans += -((-num) // a)
    bit.add(i, r, -(-((-num) // a)) * a)
print(ans)