MOD = 1_000_000_007
m, n = map(int, input().split())

def modpower_rec(a, b, M=MOD):
    # compute a^b (mod M)
    if b <= 8:
        return (a ** b) % M
    else:
        if b % 2 == 0:
            return modpower_rec(a ** 2, b // 2, M)
        else:
            return (modpower_rec(a ** 2, b // 2, M) * a) % M


def modpower_rec2(a, b, M=MOD):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return modpower_rec2((a ** 2) % M, b // 2) % M
    else:
        return (modpower_rec2((a ** 2) % M, b // 2) * a) % M


def mpower(a, b, M=MOD):
    rem = 1
    while b > 0:
        if b % 2 == 1:
            rem = rem * a % M
        a = a ** 2 % M
        b //= 2
    return rem % M

# print(modpower_rec(m, n, MOD))
# print(modpower_rec2(m, n, MOD))
print(mpower(m, n, MOD))
