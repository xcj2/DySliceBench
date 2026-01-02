def main():
    from itertools import accumulate as ac
    n = int(input())
    a = list(map(int, input().split()))

    class BIT():
        def __init__(self, n):
            self.n = n
            self.bit = [0]*(n+1)

        # 位置iに値vを足す
        def add(self, i, v):
            x = i+1
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

        # 位置iからjまでの和(sum(bit[i:j]))を計算する
        def sum_range(self, i, j):
            return self.sum(j) - self.sum(i)

    def value(v):
        if n == 1:
            if v <= a[0]:
                return True
            else:
                return False
        b = [0]+list(ac([(i >= v)*2-1 for i in a]))
        bit = BIT(2*n+1)
        ans = 0
        bit.add(b[-1]+n, 1)
        for i in range(n-1, -1, -1):
            w = b[i]
            ans += bit.sum_range(w+n, 2*n+1)
            bit.add(w+n, 1)
        if ans >= (n*(n+1)//2)//2:
            return True
        else:
            return False

    def b_search(ok, ng, value):
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if value(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(b_search(0, 10**9+1, value))


main()
