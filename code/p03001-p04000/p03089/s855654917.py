import math
from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    N = read_int()
    B = read_ints()
    answer = [0]*N
    for j in range(N-1, -1, -1):
        last_valid = -1
        for i in range(len(B)):
            if B[i] == i+1:
                last_valid = i
        if last_valid == -1:
            print(-1)
            return
        answer[j] = B.pop(last_valid)
    for a in answer:
        print(a)


if __name__ == '__main__':
    solve()
