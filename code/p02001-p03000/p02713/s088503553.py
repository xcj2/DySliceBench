import math
from typing import List, NoReturn


def sum_gcd(k: int) -> int:
    cache: List[List[List[int]]] = [[[0] * (k + 1) for i in range(k + 1)] for j in range(k + 1)]

    def cached_gcd(a: int, b: int, c: int) -> int:
        k0: int
        k1: int
        k2: int
        k0, k1, k2 = sorted([a, b, c])

        result: int = cache[k0][k1][k2]
        if result > 0:
            return result
        else:
            result = math.gcd(math.gcd(k0, k1), k2)
            cache[k0][k1][k2] = result
            return result

    answer: int = 0
    for h in range(1, k + 1):
        for i in range(1, k + 1):
            for j in range(1, k + 1):
                answer += cached_gcd(h, i, j)

    return answer


def main() -> NoReturn:
    k: int = int(input().rstrip())
    print(sum_gcd(k))


if __name__ == '__main__':
    main()
