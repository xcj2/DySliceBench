from typing import List, Dict

INF = 10**9+1


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> int:
    H, W = read_ints()
    S: List[str] = []
    for _ in range(H):
        S.append(input().strip())
    black_count = [[INF for _ in range(W)] for _ in range(H)]
    if S[0][0] == '.':
        black_count[0][0] = 0
    else:
        black_count[0][0] = 1

    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if S[i][j] == '.':
                if i > 0:
                    black_count[i][j] = min(black_count[i][j], black_count[i-1][j])
                if j > 0:
                    black_count[i][j] = min(black_count[i][j], black_count[i][j-1])
            else:
                if i > 0:
                    if S[i-1][j] == '.':
                        black_count[i][j] = min(black_count[i][j], black_count[i-1][j]+1)
                    else:
                        black_count[i][j] = min(black_count[i][j], black_count[i-1][j])
                if j > 0:
                    if S[i][j-1] == '.':
                        black_count[i][j] = min(black_count[i][j], black_count[i][j-1]+1)
                    else:
                        black_count[i][j] = min(black_count[i][j], black_count[i][j-1])
    return black_count[H-1][W-1]


if __name__ == '__main__':
    print(solve())
