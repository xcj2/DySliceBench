def iread():
    return int(input())


def sread():
    return input()


def aread_int():
    tmp = input().split()
    ret = [int(i) for i in tmp]
    return ret


def aread_str():
    return input().split()


def check(arg):
    if arg == '#':
        return 1
    else:
        return 0

def format_print(matrix, colum, row):
    for i in range(colum):
        for j in range(row):
            print(matrix[i][j], end="")
        print("")

if __name__ == '__main__':
    h, w = map(int, input().split())
    matrix = []
    ans = []
    for _ in range(h):
        ans.append([0] * w)
        
    for _ in range(h):
        matrix.append(list(input()))

    for i in range(h):
        for j in range(w):
            if check(matrix[i][j]) > 0:
                ans[i][j] = '#'
            else:
                cnt = 0
                if i > 0 and i < h - 1:
                    cnt += check(matrix[i - 1][j])
                    cnt += check(matrix[i + 1][j])
                    if j > 0:
                        cnt += check(matrix[i - 1][j - 1])
                        cnt += check(matrix[i][j - 1])
                        cnt += check(matrix[i + 1][j - 1])
                    if j < w - 1:
                        cnt += check(matrix[i - 1][j + 1])
                        cnt += check(matrix[i][j + 1])
                        cnt += check(matrix[i + 1][j + 1])
                elif i > 0:
                    cnt += check(matrix[i - 1][j])
                    if j > 0:
                        cnt += check(matrix[i - 1][j - 1])
                        cnt += check(matrix[i][j - 1])
                    if j < w - 1:
                        cnt += check(matrix[i - 1][j + 1])
                        cnt += check(matrix[i][j + 1])
                elif i < h - 1:
                    cnt += check(matrix[i + 1][j])
                    if j > 0:
                        cnt += check(matrix[i][j - 1])
                        cnt += check(matrix[i + 1][j - 1])
                    if j < w - 1:
                        cnt += check(matrix[i][j + 1])
                        cnt += check(matrix[i + 1][j + 1])
                else:
                    if j > 0:
                        cnt += check(matrix[i][j - 1])
                    if j < w - 1:
                        cnt += check(matrix[i][j + 1])

                ans[i][j] = cnt
    format_print(ans, h, w)