import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)


def read():
    H, W = map(int, input().strip().split())
    S = []
    for i in range(H):
        s = list(input().strip())
        S.append(s)
    return H, W, S


def solve(H, W, S):
    if H == 1 and  W == 1 and S[0][0] == "#":
        return "No"
    
    dd = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(y, x):
        depth = 1
        S[y][x] = "."
        for dy, dx in dd:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == "#":
                depth = max(depth, dfs(ny, nx) + 1)
        return depth

    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                depth = dfs(i, j)
                if depth == 1:
                    return "No"
    return "Yes"


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
