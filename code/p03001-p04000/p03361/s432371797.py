def solve():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    org = [[0] * W for i in range(H)]
    # 縦ループ
    for i in range(H):
        #　横ループ
        for j in range(W):
            org[i][j] = S[i][j]
            if S[i][j] == '#':
                if canPaint(i, j, S, H, W) == True:
                    continue
                else:
                    return False
            else:
                continue
    return True


def canPaint(i, j, S, H, W):
    for x in range(-1, 2):
        for y in range(-1, 2):
            # その場と斜め以外の場合
            if (x == 0 or y == 0) and (x != 0 or y != 0):
                dx = x + j
                dy = y + i
                # 移動不可能
                if dx < 0 or dx > W - 1 or dy < 0 or dy > H - 1:
                    continue
                else:
                    if S[dy][dx] == '#':
                        return True
    return False
def main():
    if solve() == True:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()

