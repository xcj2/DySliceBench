from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    S = read_int()
    dp = [[0 for _ in range(S+1)] for _ in range(S//3+1)]
    prefix = [1]*(S+1)
    new_prefix = [0]*(S+1)
    modulo = 10**9+7
    for i in range(1, S//3+1):
        for j in range(1, S+1):
            if i > 0 and j >= 3:
                dp[i][j] = (dp[i][j]+prefix[j-3])%modulo
            new_prefix[j] = (new_prefix[j-1]+dp[i][j])%modulo
        prefix, new_prefix = new_prefix, prefix
        new_prefix[0] = 0
    #dp[i][j] = dp[i-1][j-k] # i number of elements such that sum is j, 3 <= k <= 9
    return sum(dp[i][S] for i in range(1, S//3+1))%modulo


if __name__ == '__main__':
    print(solve())
