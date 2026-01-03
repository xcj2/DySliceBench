H, W, A, B = [int(_) for _ in input().split()]
p = 10 ** 9 + 7


# 二分累乗法 で n^x % p を求める
# pow(n,x,p) で得られるので次からはそっちつかう
def power(n, x, p):
    return pow(n,x,p)
    # a = n  # a^(2^0), a^(2^1), ...
    # ans = 1
    # while x > 0:
    #     if x & 1:
    #         ans = (ans * a) % p
    #     x = x >> 1
    #     a = (a ** 2) % p
    # return ans


def solve():
    kaijo = [0] * (H + W + 1)
    kaijo[0] = kaijo[1] = 1
    for i in range(2, H + W + 1):
        kaijo[i] = (i * kaijo[i - 1]) % p
    gyaku = [0] * (H + W + 1)
    gyaku[0] = gyaku[1] = 1
    for i in range(2, H + W + 1):
        gyaku[i] = power(kaijo[i], p - 2, p)

    # for i in range(H + W + 1):
    #     assert (kaijo[i] * gyaku[i]) % p == 1, (kaijo[i], gyaku[i])

    def conb(_x, _y):
        return (kaijo[_x] * gyaku[_y] * gyaku[_x - _y]) % p

    # h = H - A - 1
    # h2 = H - (H - A)
    ans = 0
    for i in range(W - B):
        ans = (ans + conb(H - A - 1 + B + i, H - A - 1) * conb(A - 1 + W - 1 - B - i, A - 1)) % p
    # for i in range(B, W):
    #     tmp1 = kaijo[h + i] * gyaku[h + i] * gyaku[h + i - max(h, i)]
    #     j = W - i - 1
    #     tmp2 = kaijo[h2 + j] * gyaku[h2 + j] * gyaku[h2 + j - max(h2, j)]
    #     ans = (ans + tmp1 * tmp2) % p
    # print(ans)
    print(ans)


if __name__ == '__main__':
    solve()