class Sieve:
    """区間[2,n]の値を素因数分解する"""

    def __init__(self, n=1):
        primes = []
        f = [0] * (n + 1)
        f[0] = f[1] = -1
        for i in range(2, n + 1):  # 素数を探す
            if f[i]: continue
            primes.append(i)
            f[i] = i  # 素数には自身を代入
            for j in range(i * i, n + 1, i):  # 合成数に素因数を書き込む
                if not f[j]:
                    f[j] = i  # 最小の素因数を代入
        self.primes = primes
        self.f = f

    def is_prime(self, x) -> bool:  # 素数判定
        return self.f[x] == x

    def factor_list(self, x) -> list:  # 素因数分解の昇順リスト, [2,2,3,5,...]
        res = []
        while x != 1:
            res.append(self.f[x])
            x //= self.f[x]
        return res

    def factor(self, x) -> list:  # 素因数分解の頻度リスト, [[2,x],[3,y],[5,z],...]
        fl = self.factor_list(x)
        if not fl: return []
        res = [[fl[0], 0]]
        for p in fl:
            if res[-1][0] == p:
                res[-1][1] += 1
            else:
                res.append([p, 1])
        return res


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    MX = 10 ** 5

    s = Sieve(MX)

    like2017 = [0] * (MX + 1)
    for x in range(1, MX + 1, 2):
        if s.is_prime(x) and s.is_prime((x + 1) // 2):
            like2017[x] = 1

    *acc, = accumulate(like2017)

    Q = int(input())

    ans = []
    for _ in range(Q):
        left, right = map(int, input().split())
        res = acc[right] - acc[left - 1]
        ans.append(res)

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()

# import sys
#
# sys.setrecursionlimit(10 ** 7)
#
# input = sys.stdin.readline
# rstrip()
# int(input())
# map(int, input().split())
