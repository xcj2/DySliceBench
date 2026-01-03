import math

from functools import lru_cache


@lru_cache(maxsize=4096)
def get_cost(x, y):
    return int(math.pow((x - y), 2))


def get_costs(target, numbers):
    return sum([get_cost(target, n) for n in numbers])


def check(n, numbers):
    n_max = max(numbers)
    n_min = min(numbers)
    costs = []
    for target in range(n_min, n_max + 1):
        costs.append(get_costs(target=target, numbers=numbers))

    return min(costs)


def main():
    N = int(input())
    numbers = list(map(int, input().split()))
    print(check(n=N, numbers=numbers))


if __name__ == '__main__':
    main()
