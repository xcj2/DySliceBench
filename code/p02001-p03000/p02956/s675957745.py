def main():
    import sys
    from operator import itemgetter
    input = sys.stdin.readline

    class Bit:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def sum(self, i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x):
            while i <= self.size:
                self.tree[i] += x
                i += i & -i

    mod = 998244353
    N = int(input())
    X_raw = [0] * N
    Y_raw = [0] * N
    for i in range(N):
        x, y = map(int, input().split())
        X_raw[i] = x
        Y_raw[i] = y

    val2idx_X = {}
    val2idx_Y = {}
    for i in range(N):
        val2idx_X[X_raw[i]] = i
        val2idx_Y[Y_raw[i]] = i
    X_raw.sort()
    Y_raw.sort()
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[val2idx_X[X_raw[i]]] = i+1
        Y[val2idx_Y[Y_raw[i]]] = i+1

    XY = [(x, y) for x, y in zip(X, Y)]
    XY.sort(key=itemgetter(0))

    bit_ul = Bit(N + 2)
    bit_ur = Bit(N+2)
    ul = []
    ur = []
    for x, y in XY:
        ul.append(bit_ul.sum(y))
        ur.append(bit_ur.sum(N+1) - bit_ur.sum(y))
        bit_ul.add(y, 1)
        bit_ur.add(y, 1)

    bit_dl = Bit(N + 2)
    bit_dr = Bit(N + 2)
    dl = []
    dr = []
    for x, y in reversed(XY):
        dl.append(bit_dl.sum(y))
        dr.append(bit_dr.sum(N + 1) - bit_dr.sum(y))
        bit_dl.add(y, 1)
        bit_dr.add(y, 1)
    dl.reverse()
    dr.reverse()

    ans = 0
    two_N = pow(2, N, mod) - 1
    for i in range(N):
        half = ((pow(2, ul[i]+ur[i], mod) + pow(2, dl[i]+dr[i], mod))%mod
                + (pow(2, ul[i]+dl[i], mod) + pow(2, ur[i]+dr[i], mod))%mod)%mod
        qu = ((pow(2, ul[i], mod) + pow(2, ur[i], mod))%mod
              +(pow(2, dl[i], mod) + pow(2, dr[i], mod))%mod)%mod
        ans = ((ans + two_N)%mod + (-half + qu)%mod)%mod

    print(ans)


if __name__ == '__main__':
    main()
