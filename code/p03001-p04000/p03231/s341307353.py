# https://atcoder.jp/contests/agc028/tasks/agc028_a

# 問題からエスパーするとlcmが答えになる
# lcmで作れないならそれ以上伸ばしても絶対作れない
import sys
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline
ra = range
enu = enumerate


def mina(*argv, sub=1): return list(map(lambda x: x - sub, argv))
# 受け渡されたすべての要素からsubだけ引く.リストを*をつけて展開しておくこと


def read_ints(): return list(map(int, read().split()))


from math import gcd


def lcm(a, b):
    # 最小公倍数
    g = gcd(a, b)
    return a // g * b


N, M = read_ints()
S = read()[:-1]
T = read()[:-1]

L = lcm(N, M)
# 衝突する文字は各文字数をgcdで割った文字ごとに出現する
s_step = N // gcd(N, M)
t_step = M // gcd(N, M)
print(L if S[::s_step] == T[::t_step] else -1)
