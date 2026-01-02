def divisors(N):
    divs = set([1, N])
    i = 2
    while i ** 2 <= N:
        if N % i == 0:
            divs.add(i)
            divs.add(N//i)
        i += 1
    return list(divs)


def is_ok(N, K):
    if K <= 1:
        return False
    while N % K == 0:
        N //= K
    return N % K == 1


def main():
    N = int(input())
    ans = 0
    for cand in divisors(N):
        if is_ok(N, cand):
            ans += 1
    for cand in divisors(N-1):
        if is_ok(N, cand):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
