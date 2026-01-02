from functools import lru_cache
import sys

sys.setrecursionlimit(10 ** 5)
MOD = 998244353


# TLE
def solve(S, K):
    numZeroes = S.count("0")
    # Count number of ones before each zero. This is a unique representation of the string
    ones = [0 for i in range(numZeroes + 1)]
    j = 0
    for x in S:
        if x == "0":
            j += 1
        else:
            assert x == "1"
            ones[j] += 1

    # The ones can move to behind an earlier zero. At most K of them can move.
    # Always best to move directly to desired location to use fewer moves
    @lru_cache(maxsize=None)
    def numWays(i, usedK, extraOnes):
        if usedK == K and extraOnes == 0:
            return 1
        if i == 0:
            # If first zero, have to use up all the extra ones
            return 1

        # Keep current value
        ways = numWays(i - 1, usedK, extraOnes)
        # Use up some extra ones to increment curr
        for j in range(1, extraOnes + 1):
            ways += numWays(i - 1, usedK, extraOnes - j)
            ways %= MOD
        # Steal some ones to decrement curr
        for j in range(1, ones[i] + 1):
            if usedK + j > K:
                break

            ways += numWays(i - 1, usedK + j, extraOnes + j)
            ways %= MOD

        return ways % MOD

    return numWays(len(ones) - 1, 0, 0) % MOD


# TLE
def solve(S, K):
    numZeroes = S.count("0")
    numOnes = len(S) - numZeroes
    # Count number of ones before each zero. This is a unique representation of the string
    ones = [0 for i in range(numZeroes + 1)]
    j = 0
    for x in S:
        if x == "0":
            j += 1
        else:
            assert x == "1"
            ones[j] += 1

    # The ones can move to behind an earlier zero. At most K of them can move.
    # Always best to move directly to desired location to use fewer moves
    K = min(K, numOnes)
    numWays = [
        [[None for extraOnes in range(numOnes + 1)] for usedK in range(K + 1)]
        for i in range(len(ones))
    ]
    for i in range(len(ones)):
        numWays[i][K][0] = 1
    for usedK in range(K + 1):
        for extraOnes in range(numOnes + 1):
            numWays[0][usedK][extraOnes] = 1
    for i in range(len(ones)):
        for usedK in range(K, -1, -1):
            for extraOnes in range(usedK, -1, -1):
                if usedK == K and extraOnes == 0:
                    continue
                if i == 0:
                    continue

                # Keep current value
                ways = numWays[i - 1][usedK][extraOnes]
                # Use up some extra ones to increment curr
                for j in range(1, extraOnes + 1):
                    ways += numWays[i - 1][usedK][extraOnes - j]
                    ways %= MOD
                # Steal some ones to decrement curr
                for j in range(1, ones[i] + 1):
                    if usedK + j > K or extraOnes + j > numOnes:
                        break

                    ways += numWays[i - 1][usedK + j][extraOnes + j]
                    ways %= MOD

                numWays[i][usedK][extraOnes] = ways % MOD

    return numWays[len(ones) - 1][0][0] % MOD


S, K = input().split()
S = list(S)
K = int(K)
print(solve(S, K))
