def main():
    from sys import stdin
    input = stdin.readline
    mod = 998244353
    n = int(input())
    xy = [list(map(int, input().split())) for _ in [0]*n]
    ans = 0
    pow_2 = [1]
    j = 1
    for i in range(n):
        j = j*2 % mod
        pow_2.append(j)
    p2 = pow_2[n-1]

    xy.sort(key=lambda x: x[1])
    xy = [(x, i+1) for i, (x, y) in enumerate(xy)]
    xy.sort()

    class BIT():
        def __init__(self, n):
            self.n = n
            self.maxbit = 2**(len(bin(self.n))-3)
            self.bit = [0]*(self.n+1)
            self.allsum = 0

        # 全ての要素に1を足す
        def all_plus(self):
            self.bit = [0]+[i & (-i) for i in range(1, self.n+1)]
            self.allsum = self.n

        # 要素iにvを追加する
        def add(self, i, v):
            x = i
            self.allsum += v
            while x < self.n + 1:
                self.bit[x] += v
                x += x & (-x)

        # 位置0からiまでの和(sum(bit[:i]))を計算する
        def sum(self, i):
            ret = 0
            x = i
            while x > 0:
                ret += self.bit[x]
                x -= x & (-x)
            return ret

    bit_left = BIT(n)
    bit_right = BIT(n)
    bit_right.all_plus()

    for i, (x, y) in enumerate(xy):
        bit_right.add(y, -1)
        A = bit_left.sum(y)
        B = i-A
        C = bit_right.sum(y)
        D = n-i-1-C
        bit_left.add(y, 1)
        ans += (pow_2[A]-1)*(pow_2[D]-1)*(pow_2[B+C])
        ans += (pow_2[B]-1)*(pow_2[C]-1)*(pow_2[A+D])
        ans -= (pow_2[B]-1)*(pow_2[C]-1)*(pow_2[A]-1)*(pow_2[D]-1)
        ans += p2
        ans = ans % mod
    print(ans)


main()
