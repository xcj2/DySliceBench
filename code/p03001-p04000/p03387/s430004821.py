def main():
    A, B, C = map(int, input().split())

    #f(A, B, C)
    editorial(A, B, C)


def editorial(A, B, C):
    """
    fより、最終値をxとするとx={max, max + 1}
    操作回数: [3x - (A+B+C)] / 2
    1回の操作で2増えるので
        差分/2が回数となる
        3x mod 2 == abc mod 2

    3max mod 2 == abc mod 2
        true: 上記の通りのあまりの一致
        false: x=max+1より、全体では3max+3より奇数増えるので一致しない
    """
    abc = [A, B, C]
    m = max(abc)
    m3 = m * 3
    s = sum(abc)

    if m3 % 2 == s % 2:
        ans = (m3 - s) // 2
    else:
        ans = (m3 + 3 - s) // 2

    print(ans)


def f(A, B, C):
    """
    A: 545, 565, 666 ans=2
    B: 445,      555 ans=1
    C: 123, 233, A pattern ans=3
    D: 135, 245, 355, 555 ans=3
    E: 235, 345, 455, A pattern ans=4
    """
    A, B, C = sorted([A, B, C])
    ans = 0
    if B != C:
        ans += C - B
        B = C
        A += ans

    diff = B - A
    ans += diff // 2
    if diff % 2 != 0:
        # A+2,BC+1
        ans += 2

    print(ans)


if __name__ == '__main__':
    main()
