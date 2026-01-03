def comb(n, r):
    return fact(n) // (fact(r) * fact(n - r))

def fact(n):
    if n < 0:
        return
    if n == 0:
        return 1
    ret = n
    for i in range(n-1, 0, -1):
        ret *= i
    return ret

def main():
    n, p = map(int, input().split())
    A = list(map(int, input().split()))
    AA = [i % 2 for i in A]
    even = AA.count(0)
    odd_cnt = n - even
    ans = 0
    if p:  # oddのとき
        for i in range(odd_cnt + 1):
            if i % 2 != 0:
                ans += comb(odd_cnt, i)
    else:  # evenのとき
        for i in range(odd_cnt + 1):
            if i % 2 == 0:
                ans += comb(odd_cnt, i)
    print(2 ** even * ans)


if __name__ == '__main__':
    main()