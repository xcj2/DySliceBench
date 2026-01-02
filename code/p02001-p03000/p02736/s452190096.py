from collections import Counter, defaultdict


N, = list(map(int, input().split()))
A = list(map(int, input()))

# Do one step to reduce the list to only 0, 1, or 2
# All subsequent steps will only contain 0, 1, or 2
A = [abs(x - y) for x, y in zip(A, A[1:])]
N -= 1


def solve(A):
    N = len(A)

    def fact(n):
        if n == 0:
            return 1
        return n * fact(n - 1)

    def nCr(n, r):
        return fact(n) // (fact(n - r) * fact(r))

    def nCrMod2(n, r):
        return 0 if (n ^ r) & r else 1
        # See https://brilliant.org/wiki/lucas-theorem/
        while r:
            if r % 2 and not n % 2:
                return 0
            n //= 2
            r //= 2
        return 1

    onlyZeroesAndTwos = Counter(A)[1] == 0

    ans = None
    if onlyZeroesAndTwos:
        ans = 2 * (sum(nCrMod2(N - 1, i) * (A[i] // 2) for i in range(N)) % 2)
    else:
        ans = sum(nCrMod2(N - 1, i) * A[i] for i in range(N)) % 2

    if False:
        import numpy as np

        # Absolute difference and mod 4 sum is almost the same:
        #         abs(x - y)   (x + y) % 4
        # 0, 0    0            0
        # 0, 2    2            2
        # 2, 2    0            0
        #
        # 0, 1    1            1
        # 1, 2    1            3
        #
        # 1, 1    0            2
        #
        # When the list only contains 0 and 2, can just use mod 4 sum exactly
        # When the mod 4 sum answer is odd, know the real answer is 1?

        # nextVec[i] = (vec[i] + vec[i + 1]) % 4
        mat = np.zeros((N, N), dtype=np.int64)
        for i in range(N - 1):
            mat[i][i] = 1
            mat[i][i + 1] = 1

        vec = np.array(A, dtype=np.int64)

        for t in range(N):
            M = np.linalg.matrix_power(mat, t)
            print("t", t)
            print("M^t", M)
            print("v_t", np.matmul(M, vec)[: N - t] % 4)
            print()
        # By inspection, it turns out the M^(N - 1) * v is just the corresponding row of the pascal triangle
        for i in range(N):
            assert np.linalg.matrix_power(mat, N - 1)[0][i] == nCr(N - 1, i)

        mod4 = sum(nCr(N - 1, i) * A[i] for i in range(N)) % 4

        # If there are no ones, mod4 is the exact answer (either 0 or 2)
        ans2 = mod4
        if not onlyZeroesAndTwos:
            # If there are ones, answer is either 0 or 1
            # The answer is 1 if mod4 is 1 or 3
            ans2 = mod4 % 2
        # Check fast and slow way
        assert ans == ans2
    return ans


print(solve(A))

if False:
    # Test
    from itertools import product

    for N in range(2, 7):
        print("N", N)

        groups = defaultdict(list)
        for A in product([0, 1, 2], repeat=N):
            temp = list(A)
            for i in range(N - 1):
                temp = [abs(x - y) for x, y in zip(temp, temp[1:])]
            assert len(temp) == 1
            groups[temp[0]].append(A)

        for k, v in groups.items():
            print("ans", k)
            for A in v:
                assert k == solve(A)
                print("\t", A)
        print()
