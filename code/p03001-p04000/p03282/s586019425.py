def main():
    """
    Si: '1' to '9'
    1 <= |S| <= 100
    1 <=  K  <= 10^18

    5000兆: 5_000_000_000_000_000
        5 * 10^15
    """
    S = input()
    K = int(input())
    ans = f(S, K)
    print(ans)


def f(S, K):
    """
    10^18 <<<<<<<<<<<< 2^(5 * 10^15)
    """
    ans = "1"
    for i, c in enumerate(S, 1):
        if c != "1":
            return c
        elif i == K:
            return "1"

    return ans


def NG(S, K):
    """
    1: 不変
    2: 2^d
        day0: 2
        day1: 22
        day2: 2222
        day3: 22222222
    """
    import datetime
    day = 5 * (10 ** 15)
    ls = {1: 1}
    for i in range(2, 9+1):
        ls[i] = i ** day
        print(i, datetime.datetime.now())

    idx = 1
    for c in S:
        idx += ls[c]
        if idx >= K:
            return c


if __name__ == '__main__':
    main()
