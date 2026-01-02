N = 8
tate = [True]*N
yoko = [True]*N
rnaname = [True]*(2*N-1)
lnaname = [True]*(2*N-1)
board = [[True]*N for i in range(N)]


def update(x, y, value):
    tate[x] = value
    yoko[y] = value
    rnaname[x+y] = value
    lnaname[x-y+N-1] = value
    board[x][y] = value


def check(x, y):
    if tate[x] and yoko[y] and rnaname[x+y] and lnaname[x-y+N-1]:
        return True
    return False


def show():
    for i in range(N):
        for j in range(N):
            print('.' if board[i][j] else 'Q', sep='', end='')
        print()


# iは縦ベース
def solve(i):
    if i == N:
        show()
        exit(0)
    if tate[i] is False:
        solve(i+1)
    for j in range(N):
        if check(i, j):
            update(i, j, False)
            solve(i+1)
            update(i, j, True)


n = int(input())
for i in range(n):
    Q = list(map(int, input().split()))
    update(Q[0], Q[1], False)

for i in range(N):
    if tate[i]:
        solve(i)
        break
solve(N)


