import sys
input = sys.stdin.readline


def read():
    H, W = map(int, input().strip().split())
    S = [['x' for j in range(W+2)] for i in range(H+2)]
    for i in range(H):
        s = input().strip()
        for j in range(W):
            S[i+1][j+1] = s[j]
    return H, W, S


def put_number(y, x, S):
    if S[y][x] == '#':
        return
    count = 0
    for dy, dx in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
        ny, nx = dy + y, dx + x
        if S[ny][nx] == '#':
            count += 1
    S[y][x] = str(count)


def solve(H, W, S):
    for i in range(1, H+1):
        for j in range(1, W+1):
            put_number(i, j, S)
    for i in range(1, H+1):
        print(''.join(S[i][1:W+1]))


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
