import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def make_divisors(n: int):
    lower_divs = []
    upper_divs = []
    i = 1
    while i**2 <= n:
        if n % i == 0:
            lower_divs.append(i)
            if i != n // i:
                upper_divs.append(n // i)
        i += 1
    return lower_divs + upper_divs[::-1]


def main():
    n = input_int()
    divs = make_divisors(n)
    ans = 0
    for div in divs:
        m = (n // div) - 1
        if m == 0:
            continue
        if n // m == n % m:
            ans += m
    print(ans)

    return


if __name__ == "__main__":
    main()
