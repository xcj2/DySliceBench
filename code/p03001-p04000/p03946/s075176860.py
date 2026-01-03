import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, T = read_ints()
    A = read_ints()
    MAX_OF_REST = []
    MAX = -math.inf
    for i in range(N-1, -1, -1):
        MAX = max(MAX, A[i])
        MAX_OF_REST.append(MAX)
    MAX_OF_REST.reverse()
    max_profit = 0
    max_count = 0
    for i in range(N-1):
        profit = MAX_OF_REST[i+1]-A[i]
        if profit > max_profit:
            max_profit = profit
            max_count = 1
        elif profit == max_profit:
            max_count += 1
    return max_count


if __name__ == '__main__':
    print(solve())
