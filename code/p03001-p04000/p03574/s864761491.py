def solve():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    c = 0
    lis = [[0]*W for i in range(H)]
    for i in range(H):
        for j in range(W):
            c = 0

            if S[i][j] == '#':
                lis[i][j] = '#'
                continue
            else:
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if k == 0 and l == 0:
                            pass
                        elif judge(i + k, j + l, W, H, S) == True:
                            c += 1
                if c == 0:
                    lis[i][j]= '0'
                else:
                    lis[i][j] = str(c)


    for i in range(H):
        print(''.join(map(str, lis[i])))

# 位置が正しいかを判定
def judge(x, y, W, H, S):
    if (x < 0 or x > H - 1 or y < 0 or y >W - 1) == True:
        return False
    else:
        if S[x][y] == '#':
            return True
        else:
            return False

def main():
    solve()


if __name__ == '__main__':
    main()

