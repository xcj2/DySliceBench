import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
from collections import deque
#======================================================#
def main():
    h, w = MII()
    ch, cw = MII()
    dh, dw = MII()
    maze = [IS() for _ in range(h)]
    dq = deque([(ch-1, cw-1)])
    check = [[-1]*w for i in range(h)]
    check[ch-1][cw-1] = 0
    count = 0

    # 判定式
    inMaze = lambda x,y: 0 <= y < h and 0 <= x < w
    isWall = lambda x,y: maze[y][x] == '#'
    isChecked = lambda x,y: check[y][x] != -1
    allCheck = lambda x,y: (not inMaze(x,y)) or isWall(x,y) or isChecked(x,y)

    # 移動先
    walk = [(0,1), (0,-1), (1,0), (-1,0)]
    warp = [(dy, dx) for dy in range(-2,3) for dx in range(-2,3)]

    while True:
        walked = []
        while dq:
            y, x = dq.popleft()
            walked.append((y, x))
            for dy, dx in walk:
                ny = y+dy
                nx = x+dx
                if allCheck(nx, ny):
                    continue
                check[ny][nx] = count
                dq.appendleft((ny, nx))

        count += 1
        for y, x in walked:
            for dy, dx in warp:
                ny = y+dy
                nx = x+dx
                if allCheck(nx, ny):
                    continue
                check[ny][nx] = count
                dq.append((ny, nx))
        if not dq:
            break

    print(check[dh-1][dw-1])

if __name__ == '__main__':
    main()