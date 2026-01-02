k = 40 # 多倍長整数内で、一整数を何bitでもつか。
MOD = 200003
list_size = 2 * MOD - 1


def n2l(num, list_size = list_size):
    "number to list"
    s = '{0:0{1}b}'.format(num, k * list_size)
    return [int(s[i-k:i], 2) for i in range(k * list_size, 0, -k)]

def l2n(ls):
    "list to number"
    return int(''.join(('{0:0{1}b}'.format(n, k) for n in reversed(ls))), 2)


def rn2l(num, list_size = list_size):
    "reversed n2l"
    s = '{0:0{1}b}'.format(num, k * list_size)
    return [int(s[i:i+k], 2) for i in range(0, k * list_size, k)]

def rl2n(ls):
    "reversed l2n"
    return int(''.join(('{0:0{1}b}'.format(n, k) for n in ls)), 2)


N = int(input())
As = sorted(map(int, input().split()))

two_pow = [1] * MOD
for i in range(1, MOD):
    two_pow[i] = two_pow[i-1] * 2 % MOD

two_pow_inv = [0] * MOD
for i, e in enumerate(two_pow[:-1]):
    two_pow_inv[e] = i

cnt = [0] * MOD # cnt[i] counts 2 ** i % P
for A in As:
    if A != 0:
        cnt[two_pow_inv[A]] += 1

cnt_conv = rn2l(rl2n(cnt) ** 2)
ans = 0
for i, cnt in enumerate(cnt_conv):
    if i < MOD:
        ans += two_pow[i] * cnt
    else:
        ans += two_pow[i - MOD + 1] * cnt

ans -= sum((A**2 % MOD for A in As))
ans //= 2
print(ans)