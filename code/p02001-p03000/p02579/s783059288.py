H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Ch -= 1
Cw -= 1
Dh, Dw = map(int, input().split())
Dh -= 1
Dw -= 1
S = [list(input()) for i in range(H)]
S[Ch][Cw] = "#"

ans = 0
warp_after = [[Ch, Cw]]
warp_before = []
queue1 = [[1,0],[-1,0],[0,1],[0,-1]]
queue2 = [
        [-2,-2],[-2,-1],[-2,0],[-2,1],[-2,2],
        [-1,-2],[-1,-1],       [-1,1],[-1,2],
        [0,-2],                       [0,2],
        [1,-2], [1,-1],        [1,1], [1,2],
        [2,-2], [2,-1], [2,0], [2,1], [2,2]
    ]

def nowRange(now):
    r = []
    for i in queue1:
        j = now[0] + i[0]
        k = now[1] + i[1]
        if H > j > -1 and W > k > -1:
            if S[j][k] == "#":
                pass
            elif j == Dh and k == Dw:
                print(ans)
                exit()
            elif S[j][k] == ".":
                S[j][k] = "#"
                r = r + [[j,k]]
    return r


def stepRange(trout):
    r = []
    for i in trout:
        r = r + nowRange(i)
    if len(r) != 0:
        return r + stepRange(r)
    else:
        return []


def nowWarp(now):
    r = []
    for i in queue2:
        j = now[0] + i[0]
        k = now[1] + i[1]
        if H > j > -1 and W > k > -1:
            if S[j][k] == "#":
                pass
            elif j == Dh and k == Dw:
                print(ans)
                exit()
            elif S[j][k] == ".":
                S[j][k] = "#"
                r = r + [[j,k]]
            
    return r


def warpRange(trout):
    r = []
    for i in trout:
        r = r + nowWarp(i)
    if len(r) != 0:
        return r
    else:
        print(-1)
        exit()


while True:
    warp_before = stepRange(warp_after) + warp_after
    ans += 1
    warp_after = warpRange(warp_before)