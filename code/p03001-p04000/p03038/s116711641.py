import math
from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    N, M = read_ints()
    A = read_ints()
    BC: List[List[int]] = []
    for _ in range(M):
        BC.append(read_ints())
    A.sort()
    BC.sort(key=lambda pair: pair[1])
    chosen = 0
    answer = 0

    def pop_bc():
        nonlocal answer
        bc = BC.pop()
        bc[0] -= 1
        if bc[0] > 0:
            BC.append(bc)
        return bc[1]

    while chosen < N:
        if A and BC:
            if A[-1] > BC[-1][1]:
                answer += A.pop()
            else:
                answer += pop_bc()
        elif A:
            answer += A.pop()
        else:
            answer += pop_bc()
        chosen += 1
    return answer


if __name__ == '__main__':
    print(solve())
