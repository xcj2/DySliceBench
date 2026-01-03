# vim: set fileencoding=utf-8:


def main():
    N = int(input())
    divisors = make_divisors(N)
    ans = 10000000000000000000000000

    if pow(divisors[-1], 2) == N:
        ans = kansuu(divisors[-1], divisors[-1])
    else:

        for idx in range(0, len(divisors)-1, 2):
            ans = min(ans, kansuu(divisors[idx], divisors[idx+1]))

    print(ans)


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


def kansuu(A, B):
    return max(len(str(A)), len(str(B)))


if __name__ == '__main__':
    main()
