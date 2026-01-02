mod = 1000000007
eps = 10**-9


def main():
    import sys
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

    N = int(input())
    A = []
    for _ in range(N):
        A.append(input().rstrip('\n'))

    TF = []
    for a in A:
        if "." not in a:
            t = f = 0
            a = int(a)
            while True:
                if a%2 == 0:
                    t += 1
                    a //= 2
                else:
                    break
            while True:
                if a%5 == 0:
                    f += 1
                    a //= 5
                else:
                    break
        else:
            a0, a1 = a.split(".")
            if int(a1) == 0:
                t = f = 0
                a0 = int(a0)
            else:
                a1 = [s for s in a1]
                while a1:
                    if a1[-1] == "0":
                        a1.pop()
                    else:
                        break
                a1 = "".join(a1)
                t = f = -len(a1)
                a0 = int("".join([a0, a1]))
            while True:
                if a0%2 == 0:
                    t += 1
                    a0 //= 2
                else:
                    break
            while True:
                if a0%5 == 0:
                    f += 1
                    a0 //= 5
                else:
                    break
        TF.append((t, f))

    Q = []
    for q in TF:
        t, f = q
        Q.append((t, f, 0))
        Q.append((-t, -f, 1))
    Q.sort(key=lambda x: x[2])
    Q.sort(key=lambda x: x[1], reverse=True)
    Q.sort(key=lambda x: x[0], reverse=True)
    bit = Bit(50)
    ans = 0
    for t, f, x in Q:
        if x == 0:
            bit.add(f+10, 1)
        else:
            ans += bit.sum(50) - bit.sum(f+10-1)
            if t <= 0 and f <= 0:
                ans -= 1
    print(ans // 2)


if __name__ == '__main__':
    main()
