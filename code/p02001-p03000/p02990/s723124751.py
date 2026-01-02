from math import factorial
import sys

input = sys.stdin.readline


class AtCoder:
    def main(self):
        N, K = map(int, input().split())
        M = N - K
        for i in range(1, K + 1):
            if M + 1 < i:
                print(0)
            else:
                a = self.combinations_count(M + 1, i)
                b = self.grouping_0_ng(K, i)
                print((b * a) % (10 ** 9 + 7))

    # 組み合わせの数
    def combinations_count(self, n, r):
        n = n
        return factorial(n) // (factorial(n - r) * factorial(r))

    # x 個のものを y 個のグループに分ける場合の数(全グループに１個以上)
    def grouping_0_ng(self, x, y):
        return self.groupint_0_ok(x - y, y)

    def groupint_0_ok(self, x, y):
        return self.combinations_count(x + y - 1, y - 1)


# Run main
if __name__ == '__main__':
    AtCoder().main()
