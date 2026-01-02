from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    N, K = read_ints()
    L, R = [], []
    for _ in range(K):
        l, r = read_ints()
        L.append(l)
        R.append(r)
    dp = [0]*N
    prefix = [0]*N
    dp[0] = 1
    prefix[0] = 1
    modulo = 998244353
    for i in range(1, N):
        for k in range(K):
            left = max(0, i-R[k])
            right = i-L[k]
            if right < 0:
                continue
            if left == 0:
                dp[i] = (dp[i]+prefix[right])%modulo
            else:
                dp[i] = (dp[i]+prefix[right]-prefix[left-1])%modulo
        prefix[i] = (prefix[i]+prefix[i-1]+dp[i])%modulo
    return dp[N-1]


if __name__ == '__main__':
    print(solve())
