from collections import defaultdict

roots = defaultdict(list)
for k in range(2, 10 ** 6 + 1):
    ki = k * k
    while ki <= 10 ** 12:
        roots[ki].append(k)
        ki *= k


def factors(n):
    fhead = []
    ftail = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            fhead.append(x)
            if x * x != n:
                ftail.append(n // x)
    return fhead + ftail[::-1]


def solve(N):
    works = set()
    # Answer seems to be anything of the form: N = (K ** i) * (j * K + 1)

    # Try every divisor of N as K ** i
    for d in factors(N):
        # If i == 1, then K == d
        k = d
        if (N // d) % k == 1:
            assert k <= N
            works.add(k)
        if d == 1:
            # If i == 0, then K ** 0 == 1, so K = (N - 1) // j, so anything that is a factor of N - 1 works
            works.update(factors(N - 1))
        elif d in roots:
            # For i >= 2, see if it's in the list of precomputed roots
            for k in roots[d]:
                if k > N:
                    break
                if (N // d) % k == 1:
                    works.add(k)
    works.discard(1)
    return len(works)


(N,) = [int(x) for x in input().split()]
print(solve(N))


if False:

    def brute(N, K):
        while N >= K:
            if N % K == 0:
                N = N // K
            else:
                N = N - K
        return N

    for N in range(2, 10000):
        count = 0
        for K in range(2, N + 1):
            temp = brute(N, K)
            if temp == 1:
                print(N, K, temp)
                count += 1
        print("##########", N, count, solve(N))
        assert count == solve(N)

