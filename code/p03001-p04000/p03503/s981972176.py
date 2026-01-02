import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def dec(digits):
    answer = 0
    for d in digits:
        answer = (answer<<1) + d
    return answer

def bitcount(n):
    answer = 0
    while n != 0:
        answer += n&1
        n >>= 1
    return answer

def solve():
    N = read_int()
    F = []
    P = []
    for _ in range(N):
        F.append(dec(read_ints()))
    for _ in range(N):
        P.append(read_ints())
    max_profit = -math.inf
    for day in range(1, 1<<10):
        profit = 0
        for i in range(N):
            profit += P[i][bitcount(F[i]&day)]
        max_profit = max(max_profit, profit)
    return max_profit


if __name__ == '__main__':
    print(solve())
