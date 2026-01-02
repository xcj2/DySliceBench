import math
from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))

def modpow(base, p, modulo):
    answer = 1
    for _ in range(p):
        answer = (answer*base)%modulo
    return answer

def solve() -> Any:
    N = read_int()
    modulo = 10**9+7
    atleast = pow(10, N, modulo)-pow(9, N, modulo)
    answer = pow(8, N, modulo)+2*atleast-pow(10, N, modulo)
    return answer%modulo


if __name__ == '__main__':
    print(solve())
