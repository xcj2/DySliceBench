from collections import deque

N = 3
M = 3
board = []
expected = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

queue = deque()
bqueue = deque()

history = set()
# todo 数字で表す
# todo 2分担作にする


def swap(x1, y1, x2, y2, b):
    # 2次元配列を浅いコピーするなんて
    t = [x[:] for x in b]
    t[x1][y1], t[x2][y2] = t[x2][y2], t[x1][y1]
    return t


def p2i(b):
    tmp = 0
    for i in range(N):
        for j in range(M):
            tmp += b[i][j] * 10**(3*i+j)
    return tmp


def bfs():
    if expected == board:
        print(0)
        exit(0)

    while len(queue):
        pazzle = queue.popleft()
        cost = bqueue.popleft()
        # 0の場所を探す
        xz = None
        yz = None
        for i in range(N):
            for j in range(M):
                if pazzle[i][j] == 0:
                    xz, yz = i, j
        # 動かすことのできる方向を全て調べる
        xm = [1, 0, 0, -1]
        ym = [0, -1, 1, 0]
        for k in range(4):
            if 0 <= xz + xm[k] < N and 0 <= yz + ym[k] < N:
                # １手動かしてあったら終了。なかったら次の手に行く。
                t = swap(xz, yz, xz + xm[k], yz + ym[k], pazzle)
                ipz = p2i(t)
                if 87654321 == ipz:
                    print(cost+1)
                    exit(0)
                # 今までに出てないならキューに追加
                if ipz not in history:
                    queue.append(t)
                    history.add(ipz)
                    bqueue.append(cost+1)


for i in range(N):
    board.append(list(map(int, input().split())))
queue.append(board)
bqueue.append(0)
bfs()
