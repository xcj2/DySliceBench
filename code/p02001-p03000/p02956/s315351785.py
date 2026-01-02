I = [int(_) for _ in open(0).read().split()]
N, X, Y = I[0], I[1::2], I[2::2]
mod = 998244353


def compress_coord(raw):
    #i_v = {}
    v_i = {}
    for i, v in enumerate(sorted(set(raw))):
        #i_v[i] = v
        v_i[v] = i
    return v_i  #, i_v


class BinaryIndexedTree():
    def __init__(self, n):
        """
        constructs binary indexed tree

        Parameters
        ----------
        n : int
            maximum index value
        """
        self.n = n
        self.dat = [0] * (n + 1)

    def sum(self, i):
        """
        returns the sum of [1, i]

        Parameters
        ----------
        i : int
            right end of the interval
        """
        s = 0
        while i:
            s += self.dat[i]
            i -= i & -i
        return s

    def add(self, i, x):
        """
        adds x to i-th element

        Parameters
        ----------
        i : int
            index
        x : int
            additional value
        """
        while i <= self.n:
            self.dat[i] += x
            i += i & -i


xi = compress_coord(X)
yj = compress_coord(Y)
X = [xi[x] for x in X]
Y = [yj[y] for y in Y]
LL = [0] * (2 * N)
LR = [0] * (2 * N)
RL = [0] * (2 * N)
RR = [0] * (2 * N)
sortXY = sorted(zip(X, Y))
bit = BinaryIndexedTree(N + 10)
for x, y in sortXY:
    LL[x] = bit.sum(y + 1)
    LR[x] = bit.sum(N + 1) - bit.sum(y + 1)
    bit.add(y + 1, 1)
bit = BinaryIndexedTree(N + 10)
for x, y in sortXY[::-1]:
    RL[x] = bit.sum(y + 1)
    RR[x] = bit.sum(N + 1) - bit.sum(y + 1)
    bit.add(y + 1, 1)
ans = N * (pow(2, N, mod) - 1) % mod
for ll, lr, rl, rr in zip(LL, LR, RL, RR):
    a = pow(2, ll + lr, mod)
    b = pow(2, rl + rr, mod)
    c = pow(2, ll + rl, mod)
    d = pow(2, lr + rr, mod)
    e = pow(2, ll, mod)
    f = pow(2, lr, mod)
    g = pow(2, rl, mod)
    h = pow(2, rr, mod)
    ans -= a + b + c + d
    ans += e + f + g + h
    ans %= mod
print(ans)
