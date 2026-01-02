ans_list = []

def main():
    while True:
        ans = solve()
        if ans == "end":
            break
        ans_list.append(ans)
    
    for ans in ans_list:
        print(ans)
    
def solve():
    W,H = map(int,input().split())
    if (H,W) == (0,0):
        return "end"
    grid = [list(map(int,input().split())) for _ in range(H)]
    for i,line in enumerate(grid):
        for j,p in enumerate(line):
            if p == 2:
                si,sj = i,j
    around = [(0,1),(1,0),(0,-1),(-1,0)]
    res = [11]
    def dfs(i=si,j=sj,d=0):
        if d == 10:
            return
        for di,dj in around:
            ni = i; nj = j; nd = d
            # すぐ次のマスに障害物がある場合は進めない
            if not(0 <= ni+di < H and 0 <= nj+dj < W):
                continue
            if grid[ni+di][nj+dj] == 1:
                continue
            ni += di; nj += dj; nd += 1

            while True:
                if grid[ni][nj] == 3:
                    res[0] = min(res[0],nd)
                    break
                # はみ出たら終わり
                if not(0 <= ni+di < H and 0 <= nj+dj < W):
                    break
                # 壁に当たったらそこを支点に探索する
                if grid[ni+di][nj+dj] == 1:
                    grid[ni+di][nj+dj] = 0
                    dfs(ni,nj,nd)
                    grid[ni+di][nj+dj] = 1
                    break
                ni += di; nj += dj
    
    dfs()
    if res[0] == 11:
        res[0] = -1
    return res[0]

main()
