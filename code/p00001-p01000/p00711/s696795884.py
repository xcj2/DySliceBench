import sys

sys.setrecursionlimit(10**6)

W = None
H = None
MMAP = None
D = [(0,1),(0,-1),(1,0),(-1,0)]

def main():
    global W,H,MMAP,D
    while True:
        W,H = map(int,input().split())
        if not W and not H:
            return
        MMAP = [[] for _ in range(H)] # tiles[y][x]
        sx,sy = 0,0
        for y in range(H):
            row = list(input())
            if "@" in row:
                sy = y
                sx = row.index("@")
            MMAP[y] = row
        # gprint(tiles)
        print(calc(sx,sy))

def calc(x,y):
    global W,H,MMAP,D

    if not (x >= 0 and x < W and y >= 0 and y < H):
        return 0
    
    if MMAP[y][x] == "v" or MMAP[y][x] == "#":
        return 0

    # gprint(MMAP)
    # input()

    ssum = 1
    MMAP[y][x] = "v"

    for dx,dy in D:
        nx = x+dx
        ny = y+dy
        ssum += calc(x+dx,y+dy)

    return ssum

def gprint(tiles):
    for r in tiles:
        print(str("|".join(r)))


if __name__ == '__main__':
    main()
