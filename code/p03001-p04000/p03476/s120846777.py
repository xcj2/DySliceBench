def calc_prime(n):
    primes = set(list(range(3, n, 2)))
    primes.add(2)
    for a in range(3, n, 2):
        for i in range(a, n):
            x = a * i
            if x >= n:
                break
            if x in primes:
                primes.remove(x)

    return primes


def collect_likes(ps):
    likes = set([p for p in ps if (p + 1) / 2 in ps])
    return likes


def line(xs, n):
    ps = list(xs)
    ps.sort()
    cs = [0] * n
    s = 0
    for i in range(n):
        if i in xs:
            cs[i] = s
            s += 1
        else:
            cs[i] = s

    return cs


def main():
    n = 10 ** 5 + 9
    primes = calc_prime(n)
    likes = collect_likes(primes)
    cums = line(likes, n)
    #print(sorted(list(primes))[:100])
    #print(sorted(list(likes))[:100])
    #print(cums[:10])

    q = int(input())
    for _ in range(q):
        l, r = [int(x) for x in input().split()]
        ans = cums[r + 1] - cums[l]
        print(ans)


main()
