from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    N = read_int()
    A = read_ints()
    min_moves = 10**18
    for positive in [False, True]:
        prefix = 0
        base = 0
        moves = 0
        for a in A:
            prefix += a
            if positive:
                if prefix+base <= 0:
                    moves += 1-(prefix+base)
                    base = 1-prefix
            else:
                if prefix+base >= 0:
                    moves += prefix+base+1
                    base = -1-prefix
            positive = not positive
        min_moves = min(min_moves, moves)
    return min_moves



if __name__ == '__main__':
    print(solve())
