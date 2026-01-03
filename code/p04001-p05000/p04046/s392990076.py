def main():

    H, W, A, B = map(int, input().split())
    mod = pow(10, 9) + 7

    v = 1
    fs = [v]
    for i in range(1, H+W-1):
        v = (v * i) % mod
        fs.append(v)

    v = invfactorial(H+W-2, mod)
    invfs = [v]
    for i in range(H+W-2, 0, -1):
        v = (v * i) % mod
        invfs.append(v)
    invfs = invfs[::-1]

    tot = (fs[H+W-2] * invfs[H-1] * invfs[W-1] ) % mod
    subtract = 0
    for b in range(B):
        v1 = (fs[H-1-A+b]*invfs[b]*invfs[H-1-A]) % mod
        v2 = (fs[A-1+W-1-b] * invfs[A-1] * invfs[W-1-b]) % mod
        subtract += v1 * v2
        subtract %= mod
    # print(tot, subtract)
    return (tot - subtract) % mod


def powquick(x, y, mod):
    if y == 0: return 1
    elif y == 1: return x % mod
    elif y % 2 == 0: return pow(powquick(x, y // 2, mod) , 2) % mod
    elif y % 2 == 1: return (x * pow(powquick(x, y // 2, mod), 2)) % mod

def invfactorial(x, mod):
    v = 1
    for i in range(1, x+1):
        v = (v * i) % mod
    return powquick(v, mod-2, mod)



if __name__ == '__main__':
    print(main())