import math
from typing import List, Counter, Tuple
from collections import Counter
from itertools import permutations


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


INF = 10**9

def solve() -> int:
    N = read_int()
    D = read_ints()
    if N>23:
        return 0
    D.sort(key=lambda d:min(d, 24-d))
    right = True
    assignment = [False]*24
    assignment[0] = True
    for d in D:
        if right:
            if assignment[d]:
                return 0
            assignment[d] = True
        else:
            if assignment[(24-d)%24]:
                return 0
            assignment[(24-d)%24] = True
        right = not right

    count = 0
    counts = []
    for i in range(1, len(assignment)+1):
        i %= 24
        if not assignment[i]:
            count += 1
        else:
            counts.append(count)
            count = 0
    return min(counts)+1
        


if __name__ == '__main__':
    print(solve())
