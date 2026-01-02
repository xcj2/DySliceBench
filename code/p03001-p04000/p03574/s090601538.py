def resolve():
    '''
    code here
    '''
    H, W = [int(item) for item in input().split()]
    grid = [input() for _ in range(H)]

    res = ['' for _ in range(H)]



    def cnt_bomb(i, j):
        cnt = 0        

        for n in [-1, 0, 1]:
            for m in [-1, 0, 1]:
                cnt += chk_bomb(i+n, j+m)

        return str(cnt)


    def chk_bomb(i, j):

        if i < 0 or  H <= i or j < 0 or W <= j:
            return 0
        elif grid[i][j] == '#':
            return 1
        else:
            return 0



    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                res[i] += '#'
            else:
                res[i] += cnt_bomb(i, j)

    for line in res:
        print(line)

if __name__ == "__main__":
    resolve()
