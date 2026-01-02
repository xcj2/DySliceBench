import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
        H,W=map(int, input().split())
        grid=[list(input()) for i in range(H)]
        for h in range(H):
            for w in range(W):
                if grid[h][w]=='#':
                    for j,k in [0,1],[0,-1],[1,0],[-1,0]:
                        nh=h+j
                        nw=w+k
                        if nh<0 or nh>=H or nw<0 or nw>=W:
                            continue
                        else:
                            if grid[nh][nw]=='#':
                                break
                            else:
                                if [j,k]==[-1,0]:
                                    return 'No'
        return 'Yes'
    print(main())
resolve()