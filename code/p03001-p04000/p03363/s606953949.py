from typing import List, Dict


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> int:
    N = read_int()
    answer = 0
    A = read_ints()
    prefix: Dict[int, int] = {0: 0}
    base = 0
    dp = [0]*(N+1)
    for i, a in enumerate(A, start=1):
        base += a
        if base in prefix:
            count = 1+dp[prefix[base]]
            dp[i] = count
        else:
            dp[i] = 0
        prefix[base] = i
    return sum(dp)


if __name__ == '__main__':
    print(solve())
