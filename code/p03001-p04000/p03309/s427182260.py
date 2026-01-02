# https://atcoder.jp/contests/abc102/tasks/arc100_a
import sys
read = sys.stdin.readline


def read_ints():
    return list(map(int, read().split()))


def read_a_int():
    return int(read())


class cumsum1d:
    def __init__(self, ls: list):
        '''
        1次元リストを受け取る
        '''
        from itertools import accumulate
        self.ls_accum = [0] + list(accumulate(ls))

    def total(self, i, j):
        # もとの配列lsにおける[i,j)の中合計
        return self.ls_accum[j] - self.ls_accum[i]


N = read_a_int()
A = read_ints()
if N == 1:
    print(0)
    exit()
B = [a - i for a, i in zip(A, range(1, N + 1))]
B.sort()

# 絶対値を区切る境目はどこがよいか？
B_cum = cumsum1d(B)
ans = 10**15
for k in range(1, N):
    tmp_sum = -B_cum.total(0, k) + B_cum.total(k, N)
    add = min((2 * k - N) * B[k - 1], (2 * k - N) * B[k])
    ans = min(ans, tmp_sum + add)


print(ans)
# 式ごちゃごちゃやったけど絶対楽な方法がある。
# 明日復習
