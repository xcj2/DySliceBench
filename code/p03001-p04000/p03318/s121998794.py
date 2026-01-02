import sys
from itertools import combinations
def input(): return sys.stdin.readline().strip()
carry = False

def f(n):
    """
    順番に貪欲するのではなく、「ある数 n 以上で n/S(n) を最小にする数 f(n) を求める」と言い換えれば
    このクエリを K 回繰り返せばよい。

    例えば n = 314159265 の場合に考えてみる。仮にf(n) = 314234567だったとしてこれが間違いであることを示しつつ
    最善手を模索してみる。
    実際これよりも小さい数で n/S(n) が小さいものが存在して、例えば 314199999である。なぜなら
    まず明らかにこれは 314234567より小さく、さらに各桁の和も後半がすべて9であることから S(n) は増加しているので
    n/S(n) は小さくなっている。

    これより、n が与えられたら f(n) は n の下の桁からどこかまで順に...999と埋めたものになる。
    """
    c = str(n)
    L = len(c)
    digit_sum = [0] * (L + 1)
    for i in range(1, L + 1): digit_sum[i] = digit_sum[i - 1] + int(c[i - 1])

    ret = n
    val = n / digit_sum[-1]
    for d in range(L - 1, -1, -1):
        N = int(c[:d] + '9' * (L - d))
        valN = N / (digit_sum[d] + 9 * (L - d))
        if val > valN:
            ret = N
            val = valN
    # 多分nの桁数を超えたところに最小値はない気がする
    return ret



def main():
    K = int(input())
    print(1)
    n = 1
    for _ in range(1, K):
        n = f(n + 1)
        print(n)


if __name__ == "__main__":
    main()
