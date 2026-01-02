import sys
sys.setrecursionlimit(1 << 25)
readline = sys.stdin.buffer.readline
read = sys.stdin.readline  # 文字列読み込む時はこっち
ra = range
enu = enumerate


def exit(*argv, **kwarg):
    print(*argv, **kwarg)
    sys.exit()


def mina(*argv, sub=1): return list(map(lambda x: x - sub, argv))
# 受け渡されたすべての要素からsubだけ引く.リストを*をつけて展開しておくこと


def a_int(): return int(readline())


def ints(): return list(map(int, readline().split()))


def _make_minimum_prime(N: int):
    # xの最小の素因数表を作成
    min_prime = [x for x in range(N + 1)]
    # min_prime[0] = 0  # 0と1は素数ではない
    # min_prime[1] = 1
    for i in range(2, int(N ** 0.5) + 1):
        if min_prime[i] == i:  # 素数だったら更新
            for j in range(2 * i, N + 1, i):  # iの倍数は素数でない
                if min_prime[j] == j:
                    min_prime[j] = i
    return min_prime


min_prime = _make_minimum_prime(10**6)


from collections import Counter


def fast_factorization(N: int):
    # -> List[Tuple[int,int]] (素数,冪数)を格納
    # 最小素数配列min_primeを使ってO(log N)で因数分解
    if N == 1:
        return Counter()  # 1は素数ではない
    # 素因数分解
    arr = []
    tmp = N
    while tmp != 1:
        p = min_prime[tmp]
        tmp //= p
        arr.append(p)

    return Counter(arr)


MOD = 10**9 + 7
INF = 2**31  # 2147483648 > 10**9
# default import
from collections import defaultdict, Counter, deque
import random
from math import gcd


N = a_int()
A = ints()
random.shuffle(A)

# setかはすぐわかる
# setでなければ not coprime
# pairは互いに素かをみればいいのか
# つまり因数分解して足してったときにすべての素数のべき数が1以下であれば良い

g_set = 0
cnt = defaultdict(lambda: 0)
flg = 1  # pairwiseであるフラグ
for a in A:
    g_set = gcd(g_set, a)
    if flg:
        for p, n in fast_factorization(a).items():
            if cnt[p] != 0:
                flg = 0
            cnt[p] += n


# print(cnt)
# for v in cnt.values():
#     if v > 1:
#         flg = 0
#         break

if g_set > 1:
    print('not coprime')
elif flg:
    print('pairwise coprime')
else:
    print('setwise coprime')
