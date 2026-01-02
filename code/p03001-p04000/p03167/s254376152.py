ROUTE, WALL = 0, 1
def main():
    H, W = [int(n) for n in input().split()]
    H, W = H+1, W+1
    grid = [[ROUTE]*W for i in range(H)]
    for h in range(H):
        if h == 0:
            grid[0] = [WALL] * W
            continue
        instr = "#" + input()
        for w, c in enumerate(instr):
            grid[h][w] = ROUTE if c == "." else WALL
    dp = [-1]*(H*W)
    dp[coord_to_num(W, 1,1)]=1
    for crd in range(H*W):
        if dp[crd] != -1:
            continue
        h, w = num_to_coord(W, crd)
        if grid[h][w] == WALL:
            dp[crd] = 0
            continue
        up = dp[coord_to_num(W,h-1, w)]
        down = dp[coord_to_num(W, h, w-1)]
        dp[coord_to_num(W, h, w)] = up+down
    print(dp[coord_to_num(W, H-1, W-1)] % (10 ** 9 + 7))


def num_to_coord(W, num):
    return (num//W, num%W)
def coord_to_num(W, h, w):
    return h * W + w

if __name__ == "__main__":
    main()