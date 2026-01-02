mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.buffer.readline

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

        def lower_bound(self, w):
            if w <= 0:
                return 0
            x = 0
            k = 1 << (self.size.bit_length() - 1)
            while k:
                if x + k <= self.size and self.tree[x + k] < w:
                    w -= self.tree[x + k]
                    x += k
                k >>= 1
            return x + 1

    for _ in range(int(input())):
        N = int(input())
        Llike = []
        Rlike = []
        ans = 0
        for _ in range(N):
            k, l, r = map(int, input().split())
            if l > r:
                Llike.append([l-r, k])
                ans += l
            elif r > l:
                if k == N:
                    ans += l
                else:
                    Rlike.append([r-l, N-k])
                    ans += r
            else:
                ans += r
        bitL = Bit(len(Llike))
        bitR = Bit(len(Rlike))
        Llike.sort(key=lambda x: x[0], reverse=True)
        Rlike.sort(key=lambda x: x[0], reverse=True)
        for i in range(len(Llike)):
            bitL.add(i+1, 1)
        for i in range(len(Rlike)):
            bitR.add(i+1, 1)
        for v, k in Llike:
            if k > len(Llike):
                k = len(Llike)
            u = bitL.sum(k)
            if u == 0:
                ans -= v
                j = bitL.lower_bound(bitL.sum(len(Llike)))
                bitL.add(j, -1)
            else:
                j = bitL.lower_bound(u)
                bitL.add(j, -1)
        for v, k in Rlike:
            if k > len(Rlike):
                k = len(Rlike)
            u = bitR.sum(k)
            if u == 0:
                ans -= v
                j = bitR.lower_bound(bitR.sum(len(Rlike)))
                bitR.add(j, -1)
            else:
                j = bitR.lower_bound(u)
                bitR.add(j, -1)
        print(ans)


if __name__ == '__main__':
    main()
