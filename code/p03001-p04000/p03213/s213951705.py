def f(n):
    # prime factorization of n!
    pf = [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        cur = i
        for j in range(2, i + 1):
            while cur % j == 0:
                pf[j] += 1
                cur //= j
    return pf


def num(m, pf):
    return len(list(filter(lambda x: x >= m - 1, pf)))


def main():
    N = int(input())
    pf = f(N)
    ans = num(75, pf)
    ans += num(25, pf) * (num(3, pf) - 1)
    ans += num(15, pf) * (num(5, pf) - 1)
    ans += num(5, pf) * (num(5, pf) - 1) * (num(3, pf) - 2) // 2
    print(ans)


if __name__ == '__main__':
    main()
