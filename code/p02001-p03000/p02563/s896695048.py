class Convolution:
    sum_e = (911660635, 509520358, 369330050, 332049552, 983190778, 123842337, 238493703, 975955924, 603855026, 856644456, 131300601, 842657263, 730768835, 942482514, 806263778, 151565301, 510815449, 503497456, 743006876, 741047443, 56250497, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sum_ie = (86583718, 372528824, 373294451, 645684063, 112220581, 692852209, 155456985, 797128860, 90816748, 860285882, 927414960, 354738543, 109331171, 293255632, 535113200, 308540755, 121186627, 608385704, 438932459, 359477183, 824071951, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ROOT = 3
    def __init__(self, mod):
        self.MOD = mod

    def __butterfly(self, arr):
        n = len(arr)
        h = (n - 1).bit_length()
        MOD = self.MOD
        for ph in range(1, h + 1):
            w = 1 << (ph - 1)
            p = 1 << (h - ph)
            now = 1
            for s in range(w):
                offset = s << (h - ph + 1)
                for i in range(p):
                    l = arr[i + offset]
                    r = arr[i + offset + p] * now
                    arr[i + offset] = (l + r) % MOD
                    arr[i + offset + p] = (l - r) % MOD
                now *= Convolution.sum_e[(~s & -~s).bit_length() - 1]
                now %= MOD

    def __butterfly_inv(self, arr):
        n = len(arr)
        h = (n - 1).bit_length()
        MOD = self.MOD
        for ph in range(1, h + 1)[::-1]:
            w = 1 << (ph - 1)
            p = 1 << (h - ph)
            inow = 1
            for s in range(w):
                offset = s << (h - ph + 1)
                for i in range(p):
                    l = arr[i + offset]
                    r = arr[i + offset + p]
                    arr[i + offset] = (l + r) % MOD
                    arr[i + offset + p] = (MOD + l - r) * inow % MOD
                inow *= Convolution.sum_ie[(~s & -~s).bit_length() - 1]
                inow %= MOD

    def __call__(self, a, b):
        n = len(a)
        m = len(b)
        MOD = self.MOD
        if not n or not m: return []
        if min(n, m) <= 50:
            if n < m:
                n, m = m, n
                a, b = b, a
            res = [0] * (n + m - 1)
            for i in range(n):
                for j in range(m):
                    res[i + j] += a[i] * b[j]
                    res[i + j] %= MOD
            return res
        z = 1 << (n + m - 2).bit_length()
        a += [0] * (z - n)
        b += [0] * (z - m)
        self.__butterfly(a)
        self.__butterfly(b)
        for i in range(z):
            a[i] *= b[i]
            a[i] %= MOD
        self.__butterfly_inv(a)
        a = a[:n + m - 1]
        iz = pow(z, MOD - 2, MOD)
        for i in range(n + m - 1):
            a[i] *= iz
            a[i] %= MOD
        return a




def atcoder_practice2_f():
    import sys
    input = sys.stdin.buffer.readline

    N, M = map(int, input().split())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    convolution = Convolution(998244353)
    print(*convolution(A, B))


if __name__ == "__main__":
    atcoder_practice2_f()
