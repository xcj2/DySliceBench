def gcd1(a, b):
    def calc(a, b, first, second):
        if a < b:
            a, b = b, a
        r = a % b
        q = -(a - r)//b
        if r == 0:
            return b, second
        # first += q * second
        first = [x + q * y for (x, y) in zip(first, second)]
        return calc(r, b, second, first)
    first = [1, 0]
    second = [0, 1]
    return calc(a, b, first, second)

def mod_inv(n, mod):
    table = gcd1(n, mod)
    inv = table[1][1]
    if inv < 0:
        inv += mod
    return inv

def cmb(n, r, mod):
    ans = 1
    for i in range(r):
        ans = (ans * n) % mod
        n -= 1
    ans1 = 1
    for i in range(1, r + 1):
        ans1 = (ans1 * i) % mod
    return ans * mod_inv(ans1, mod)

def main():
    m = 10**9 + 7
    X, Y = map(int, input().split())
    XY = X + Y
    min_xy = XY // 3
    max_xy = XY - min_xy
    if XY % 3 != 0:
        print(0)
        return
    if X < min_xy or X > max_xy or Y < min_xy or Y > max_xy:
        print(0)
        return
    index_x = X - min_xy
    index_y = Y - min_xy
    # print(index_x, index_y)
    ans = cmb(min_xy, index_x, m)
    print(ans % m)


if __name__ == '__main__':
    main()

