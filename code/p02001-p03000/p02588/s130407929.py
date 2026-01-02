N, *A = open(0).read().split()


class BIT():
    def __init__(self, n, x=1):
        self.n = n
        self.T = [[0]*20 for _ in [0]*20]

    def add(self, i, y, x):
        i += 1
        y += 1
        while i <= self.n:
            j = y
            while j <= self.n:
                self.T[i][j] += x
                j += j & -j
            i += i & -i

    def _sum(self, i, y):
        i += 1
        y += 1
        ret = 0
        while i > 0:
            j = y
            while j > 0:
                ret += self.T[i][j]
                j ^= j & -j
            i ^= i & -i
        return ret

    def sum(self, i, j):
        return self._sum(18, 18) - self._sum(i-1, 18) - self._sum(18, j-1) + self._sum(i-1, j-1)


ans = 0
B = BIT(19)


def fact(n):
    cnt2 = cnt5 = 0
    for _ in range(18):
        if n % 2:
            break
        n //= 2
        cnt2 += 1
    for _ in range(18):
        if n % 5:
            break
        n //= 5
        cnt5 += 1
    return cnt2, cnt5


for a in A:
    if '.' in a:
        a, b = a.split('.')
        cnt2 = cnt5 = 9 - len(b)

        a = int(a) * (10**len(b)) + int(b)
        c2, c5 = fact(a)
        cnt2 += c2
        cnt5 += c5
    else:
        cnt2 = 9
        cnt5 = 9

        a = int(a)
        c2, c5 = fact(a)
        cnt2 += c2
        cnt5 += c5

    cnt2 = min(18, cnt2)
    cnt5 = min(18, cnt5)

    ans += B.sum(18-cnt2, 18-cnt5)
    B.add(cnt2, cnt5, 1)

print(ans)
