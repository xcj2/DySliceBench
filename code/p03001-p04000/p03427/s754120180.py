def poyo():
    ans = -1
    A = []
    for i in range(1, 100):
        t = sum([ord(x) - ord('0') for x in str(i)])
        ans = max(ans, t)
        A.append(ans)
        # print(ans)

    import numpy as np
    maxi, cnt = np.unique(A, return_counts=True)
    print(maxi)
    print(np.cumsum(cnt))
    for x, y in zip(maxi, np.cumsum(cnt)):
        print(x, y)


def naive(N):
    ans = -1
    for i in range(N + 1):
        t = sum([ord(x) - ord('0') for x in str(i)])
        ans = max(ans, t)
    return ans


# poyo()
import math


def solve(N):
    if N < 10:
        return (N)
    else:
        ans = (len(str(N + 1)) - 1) * 9
        ans += ord(str(N + 1)[0]) - ord('0') - 1
        return (ans)


def check():
    for i in range(10000):
        # print(i)
        assert solve(i) == naive(i)


N = int(input())
print(solve(N))
