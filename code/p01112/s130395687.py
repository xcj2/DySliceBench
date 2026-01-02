import sys
from itertools import combinations

def dfs(idx,N,win_cnt,will_match):
    if(idx==N):
        #win_cntがすべて(N-1)/2なら1を返す
        return 1
    
    need_win = (N-1)//2 - win_cnt[idx] #引き分けにするための必要勝数
    need_lose = len(will_match[idx]) - need_win
    # print(need_win,need_lose,(len(will_match[idx]),win_cnt[idx]))
    if(need_win > len(will_match[idx]) or need_win < 0): # 残りの試合をどう戦っても、引き分けにならない
        return 0
    res = 0
    # print(idx,"が負ける必要がある",need_lose)
    for it in combinations(will_match[idx],need_lose): ##負け試合をピッタリ必要なだけ選ぶ
        tmp = win_cnt.copy() ##勝数をいじるので現状保存
        # print(idx,win_cnt)
        # print(list(it))
        for i in it:
            # print("i",i)
            tmp[i] += 1 ## idx番目のチームの負けなので相手チームの勝数を1増やす
        res += dfs(idx+1,N,tmp,will_match)
    
    return res
def solve(N):
    M=int(input())
    # print(N,M)
    XY = [[int(i)-1 for i in input().split()] for _ in range(M)]
    win_cnt = [0]*N #チームiが何回勝ったか

    match = [[-1]*N for _ in range(N)]
    for x,y in XY:
        match[x][y] = 1
        match[y][x] = 0
        win_cnt[x]+=1
        if(x>y):
            x,y = y,x
    will_match = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            if(match[i][j]==-1): #戦ってない
                will_match[i].append(j)
    # print(*match,sep="\n")
    # print(win_cnt)
    # print(*will_match,sep="\n")
    ans = dfs(0,N,win_cnt,will_match)

    print(ans)
        


def main():
    input = sys.stdin.readline
    while True:
        N = int(input())
        if(not N):
            break
        solve(N)
if __name__ == "__main__":
    main()
