import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
from collections import deque
#======================================================#
def main():
    h, w = MII()
    ch, cw = MII()
    dh, dw = MII()
    maze = [IS() for _ in range(h)]
    check = [[-1]*w for i in range(h)]
    dq = deque([(ch-1, cw-1)])
    check[ch-1][cw-1] = 0
    count = 0

    inMaze = lambda x,y: 0 <= y < h and 0 <= x < w
    isWall = lambda x,y: maze[y][x] == '#'
    isChecked = lambda x,y: check[y][x] != -1

    while True:
        tmp = []
        while dq:
            y, x = dq.popleft()
            tmp.append((y, x))
            for dy, dx in ((0,1), (0,-1), (1,0), (-1,0)):
                ny = y+dy
                nx = x+dx
                if not inMaze(nx, ny):
                    continue
                if isWall(nx, ny):
                    continue
                if isChecked(nx, ny):
                    continue
                check[ny][nx] = count
                dq.appendleft((ny, nx))

        count += 1
        for y, x in tmp:
            for i in range(-2,3):
                for j in range(-2,3):
                    ny = y+i
                    nx = x+j
                    if not inMaze(nx, ny):
                        continue
                    if isWall(nx, ny):
                        continue
                    if isChecked(nx, ny):
                        continue
                    check[ny][nx] = count
                    dq.append((ny, nx))
        if not dq:
            break

    print(check[dh-1][dw-1])

if __name__ == '__main__':
    main()