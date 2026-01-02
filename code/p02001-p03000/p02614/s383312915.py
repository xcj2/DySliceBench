import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def contBlack(g, h, w):
    cnt = 0
    for i in range(h):
        for j in range(w):
            if g[i][j] == '#':
                cnt += 1
    return cnt

def turnrow(g, a, w):
    for j in range(w):
        g[a][j] = 'R'



def turnclumn(g, a, h):
    for i in range(h):
        g[i][a] = 'R'

from copy import deepcopy

def main():
    H, W, K = map(int, readline().split())
    grid = []
    for _ in range(H):
        grid.append(list(input()))

    cnt = 0
    for i in range(1<<H):           
        G = deepcopy(grid)
        for j in range(H):
            if (i>>j) & 1:
                turnrow(G, j, W)

        for k in range(1<<W):
            Gg = deepcopy(G)
            for l in range(W):
                if (k>>l) & 1:
                    turnclumn(Gg, l, H)
            
            # for i in range(H):
            #     print(Gg[i])
            # print()

            if contBlack(Gg, H, W) == K:
                cnt += 1

    print(cnt)
if __name__ == '__main__':
    main()
