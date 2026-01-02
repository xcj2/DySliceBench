def gcd(a: int, b: int) -> int:
    """a, bの最大公約数(greatest common divisor: GCD)を求める
    計算量: O(log(min(a, b)))
    """
    if b == 0:
        return a
    return gcd(b, a%b)


class Ruiseki_lr:
    """左右からの畳み込みをそれぞれ計算する"""
    def __init__(self, array, op, e):
        self.op = op
        self.e = e

        n = len(array)
        self.left = [e] * (n + 1)
        self.right = [e] * (n + 1)
        for i in range(n):
            self.left[i + 1] = self.op(self.left[i], array[i])
        for i in reversed(range(n)):
            self.right[i] = self.op(self.right[i + 1], array[i])

    def left(self, p):
        """区間[0, p)の畳み込み結果を返す"""
        return self.left[p]

    def right(self, p):
        """区間[p, n)の畳み込み結果を返す"""
        return self.right[p]

    def fold(self, p):
        """p番目を除いた区間[0, n)の畳み込み結果を返す"""
        return self.op(self.left[p], self.right[p + 1])

n = int(input())
a = list(map(int, input().split()))

ru = Ruiseki_lr(a, gcd, 0)
max_ = 0
for i in range(n):
    max_ = max(ru.fold(i), max_)
print(max_)