import math
from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))

def ceil(a, b):
    if a%b == 0:
        return a//b
    return a//b+1

def solve() -> Any:
    N, H = read_ints()
    A = 0
    answer = 0
    B = []
    for _ in range(N):
        a, b = read_ints()
        A = max(A, a)
        B.append(b)
    B.sort()
    while B and B[-1] > A:
        H -= B.pop()
        answer += 1
        if H <= 0:
            return answer
    return answer+ceil(H, A)


if __name__ == '__main__':
    print(solve())
