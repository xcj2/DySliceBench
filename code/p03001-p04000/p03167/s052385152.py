

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    H, W = read_ints()
    modulo = 10**9+7
    board = []
    for _ in range(H):
        board.append(input().strip())
    count = [[0]*W for _ in range(H)]
    count[0][0] = 1
    for i in range(H):
        for j in range(W):
            if board[i][j] == '.':
                if j > 0 and board[i][j-1] == '.':
                    count[i][j] = (count[i][j]+count[i][j-1])%modulo
                if i > 0 and board[i-1][j] == '.':
                    count[i][j] = (count[i][j]+count[i-1][j])%modulo
    return count[-1][-1]


if __name__ == '__main__':
    print(solve())
