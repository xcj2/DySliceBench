# Settings
mod = 10**9+7


# Preparation
def inv(a, mod):
    r = [1, 0, a]
    w = [0, 1, mod]
    while w[2] != 1:
        q = r[2]//w[2]
        r_new = [r[0]-q*w[0], r[1]-q*w[1], r[2]-q*w[2]]
        r = w
        w = r_new
    x, y = w[0], w[1]    # a*x+y*mod = 1
    return (mod+x % mod) % mod


max_num = 5*10**5+2  # 10**6 にしたほうがよい?
fact = [0 for _ in range(max_num)]
ifact = [0 for _ in range(max_num)]

fact[0] = fact[1] = 1
ifact[0] = ifact[1] = 1

for i in range(2, max_num):
    fact[i] = fact[i-1] * i % mod

ifact[max_num-1] = inv(fact[max_num-1], mod)

for i in range(2, max_num):
    ifact[max_num-i] = (ifact[max_num-i+1] * (max_num-i+1)) % mod


def comb(x, y):
    if x < 0 or y < 0 or x < y:
        return 0
    else:
        return fact[x] * ifact[y] * ifact[x-y] % mod


# Code
def solve():
    tmp = 0
    for i in range(1, n+1):
        tmp2 = comb(n, i) * fact[m-i] * ifact[m-n]
        tmp2 %= mod
        tmp += (-1)**(i-1)*tmp2

    tmp = fact[m]*ifact[m-n] - tmp
    tmp %= mod

    ans = tmp*fact[m]*ifact[m-n]
    ans %= mod

    return ans


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(solve())
