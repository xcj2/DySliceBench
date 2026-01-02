
from collections import deque
def main():
    H,W = map(int, input().split())
    start = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    field = [input() for _ in range(H)]

    wmap = [[-1] * W for _ in range(H)]
    wmap[start[0]-1][start[1]-1] = 0

    d = deque()
    d.appendleft((start[1]-1,start[0]-1))

    warpd = d.copy()

    def flood():
        while len(d) > 0:
            pos = d.pop()
            warpd.append(pos)
            posx, posy = pos
            w = wmap[posy][posx]
            for x,y in [(posx-1, posy), (posx+1, posy), (posx, posy-1), (posx, posy+1)]:
                if 0 <= x < W and 0 <= y < H and field[y][x] == "." and wmap[y][x] == -1:
                    wmap[y][x] = w
                    d.appendleft((x,y))
                    warpd.append((x,y))

    # くばる
    def warp():
        movable = set()
        while len(warpd) > 0:
            x,y = warpd.pop()
            w = wmap[y][x]
            
            for my in range(-2, 3):
                for mx in range(-2, 3):
                    px = x + mx
                    py = y + my
                    if 0 <= px < W and 0 <= py < H and field[py][px] == "." and wmap[py][px] == -1:
                        wmap[py][px] = w+1
                        movable.add((px,py))

        for item in movable:
            d.append(item)

    while len(d) != 0 and wmap[goal[0]-1][goal[1]-1] == -1:
        flood()
        warp()

    print(wmap[goal[0]-1][goal[1]-1])

if __name__ == "__main__":
    main()
