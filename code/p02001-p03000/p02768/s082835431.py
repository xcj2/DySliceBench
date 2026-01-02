from sys import stdin


def pow_mod(base, exp, mod):
    if exp == 0:
        return 1

    if exp % 2 == 0:
        t = pow_mod(base, exp/2, mod)
        return t*t % mod
    else:
        # ans=pow_mod(base, exp-1, mod)
        return (base*pow_mod(base, exp-1, mod)) % mod


def modinv(base, mod):
    return pow_mod(base, mod-2, mod)


def cmb(n, k, mod):
    p = 1
    for i in range(n-k+1, n+1):
        p = (p * i) % mod
    d = 1
    for i in range(1, k+1):
        d = (d * i) % mod
    return (p * modinv(d, mod)) % mod


mod = 7+10**9

# S = stdin.readline().rstrip().split()
# N = [int(x) for x in stdin.readline().rstrip().split()][0]
n, a, b = [int(x) for x in stdin.readline().rstrip().split()]
ans = pow_mod(2, n, mod)
ans = (ans-cmb(n, a, mod)) % mod
ans = (ans-cmb(n, b, mod)) % mod
print(ans-1)
# print(cmb(n, b, p))
# print()
