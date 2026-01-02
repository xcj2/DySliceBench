#!/usr/bin/env python


def get_all_values(N, v):
    all_values = []

    current = v
    while current <= N:
        all_values.append(current)
        current *= v

    return all_values


def get_min_number(memo, all_values, N):
    if N in memo:
        return memo[N]

    if N in all_values:
        return 1
    elif N < 6:
        return N
    else:
        min_number = min(
            [get_min_number(memo, all_values, N - v) + 1 for v in all_values if N - v > 0]
        )
        memo[N] = min_number
        return min_number


def solve(N):
    # Get all values and sort in descent order
    all_values = [1] + get_all_values(N, 6) + get_all_values(N, 9)
    sorted_all_values = list(reversed(sorted(all_values)))

    # Recursively get minimum number
    memo = {}
    ans = get_min_number(memo, sorted_all_values, N)

    return ans


def main():
    # Input
    N = int(input())

    # Solve
    ans = solve(N)

    # Answer
    print(ans)


if __name__ == "__main__":
    main()
