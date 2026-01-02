import itertools
import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


# MOD = 998244353


def toint(l, r):
    return int(''.join(map(str, S[l:r])))


def test():
    ans = 0
    for l, r in itertools.combinations_with_replacement(range(N), r=2):
        s = toint(l, r + 1)
        ans += s % P == 0
    print(ans)


def solve25():
    ret = 0
    for d in range(N):
        if S[d] % P == 0:
            ret += d + 1
    return ret


def mod_invs(max, mod):
    """
    逆元 0, 1/1, 1/2, 1/3, ..., 1/max
    :param int max:
    :param int mod:
    """
    invs = [1] * (max + 1)
    invs[0] = 0
    for x in range(2, max + 1):
        invs[x] = (-(mod // x) * invs[mod % x]) % mod
    return invs


N, P = list(map(int, sys.stdin.buffer.readline().split()))
S = list(map(int, list(sys.stdin.buffer.readline().decode().rstrip())))

# 10 mod P で割れない
if P in [2, 5]:
    ans = solve25()
    print(ans)
    exit()

# test()

powers = []
p = 1
for _ in range(N):
    powers.append(p)
    p = p * 10 % P
# int(S[1:1]), int(S[1:2]), int(S[1:3]), ...
s_additions = [0]
s = 0
for i in range(1, N):
    s = (s * 10 + S[i]) % P
    s_additions.append(s)
invs = mod_invs(max=P - 1, mod=P)


def to_index(i, p):
    # もともと x だったのが、i 番目で p になっているときの x を返す
    if i == 0:
        return p % P
    return (p - s_additions[i]) * invs[powers[i]] % P


mod_counts = [0] * P
ans = 0
for i, c in enumerate(S):
    mod_counts[to_index(i, c)] += 1
    ans += mod_counts[to_index(i, 0)]
print(ans)
