import functools

N = input()
K = int(input())

@functools.lru_cache(maxsize=2048)
def nCk(n, k):
    if k == 0:
        return 0
    elif k == 1:
        return n
    elif k == 2:
        return (n * (n-1)) // 2
    return (n * (n-1) * (n-2)) // 6

def slowsolve(N, K):
    if not N:
        return 0, {}
    ans = 0
    meta = {}
    for i in range(1, int(N) + 1):
        if len(str(i)) - str(i).count("0") == K:
            meta.setdefault(len(str(i)), 0)
            meta[len(str(i))] += 1
            ans += 1
    return ans, meta

def clean(N):
    clean_N = []
    for n in N:
        if n == "0" and not clean_N:
            pass
        else:
            clean_N.append(n)
    if clean_N:
        return "".join(clean_N)
    return ""

@functools.lru_cache(maxsize=2048)
def solve(N, K):
    N = clean(N)

    if len(N) <= 3:
        return slowsolve(N, K)[0]
    elif K == 0:
        return 0
    else:
        m = int(N[0])

        # 一番上を0にする
        ans = solve("9" * len(N[1:]), K)

        if K == 3:
            # 一番上を1 ~ m - 1にする
            # => 下の部分から2か所選び、それぞれ1 ~ 9
            ans += (m - 1) * nCk(len(N[1:]), 2) * 9 * 9
            # 一番上をmにする
            ans += solve(N[1:], K - 1)
        elif K == 2:
            # 一番上を1 ~ m - 1にする
            # => 下の部分から1か所選び、1 ~ 9
            ans += (m - 1) * len(N[1:]) * 9
            # 一番上をmにする
            ans += solve(N[1:], K - 1)
        elif K == 1:
            # 一番上をmにする
            ans += m
        return ans


print(solve(N, K))