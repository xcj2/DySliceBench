from sys import stdin
from itertools import accumulate


def fin(f):
    """
    INput with Function
    f(input())と同じ。書きやすさのために作成した。
    :param f: 入力に対して呼び出す関数
    :return: 関数の処理結果
    """
    return f(stdin.readline().rstrip())


def gin(f, nl=1):
    """
    INput with function and Generator
    空白区切りの入力の各値に対して関数fを用いて初期化を行う。
    複数行にも対応。
    使い方:
      一行の入力例 -> next(gin(int))
      複数行の入力をリストに格納する例 -> list(gin(int, n))
      forループで使う例 -> for l, r in gin(int, n):
    :param f: 各値に適応する関数
    :param nl: 行数(デフォルトは1)
    :returns: 空白区切りのリストたち
    """
    for _ in range(nl):
        yield list(map(f, stdin.readline().split()))


n, q = next(gin(int))

s = input()


def count(total, i):
    return total + 1 if s[i-1:i+1] == 'AC' else total


cumsum = list(accumulate([0] + list(range(n)), count))[1:]

for l, r in gin(int, q):
    print(cumsum[r-1] - cumsum[l-1])

