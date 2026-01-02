def main ():
    H, W = map(int, input().split())
    MAP = [list('#' for i in range(W + 2)) for j in range(H + 2)]
    for i in range(H):
        line = list(input())
        for j, dot in enumerate(line):
            MAP[i + 1][j + 1] = dot
    L = [[0 for j in range(W + 2)] for i in range(H + 2)]


    def line(MAP):
        for i in range(1, H + 2):
            before = 0
            for j in range(1, W + 2):
                if MAP[i][j] == '#':
                    for x in range(before + 1, j):
                        L[i][x] = j - before - 1
                    before = j


    def column(MAP2):
        ans = 0
        for j in range(1, W + 2):
            before = 0
            for i in range(1, H + 2):
                if MAP2[i][j] == '#':
                    for y in range(before + 1, i):
                        ans = max(ans, i - before - 1 + L[y][j])
                    before = i
        return ans - 1

    line(MAP)
    column(MAP)
    print(column(MAP))

if __name__ == '__main__':
    main()