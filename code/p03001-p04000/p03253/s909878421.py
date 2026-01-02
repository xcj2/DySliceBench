def main():
    from operator import mul
    from functools import reduce
    def cmb(n, r):
        r = min(n - r, r)
        if r == 0: return 1
        over = reduce(mul, range(n, n - r, -1))
        under = reduce(mul, range(1, r + 1))
        return over // under
    def factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])
        if temp != 1:
            arr.append([temp, 1])
        if arr == []:
            arr.append([n, 1])
        return arr

    large_p = 10 ** 9 + 7
    n, m = map(int, input().split())
    mp = factorization(m)
    r = 1
    for mpe in mp:
        tmp = cmb(mpe[1] + n - 1, n - 1)
        r = r * tmp
        r = r % large_p
    if r < 0:
        r += large_p
    if m == 1:
        print(1)
    else:
        print(r)

if __name__ == '__main__':
    main()