def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

H,W = two_int()

maps = [list(input()) for i in range(H)]

import copy 
temp_maps = copy.deepcopy(maps)

#start調査
def solve(W,H,maps):
    start_X=0
    start_Y=0
    for x in range(W):
        for y in range(H):
            count=0

            if maps[y][x]=="#":
                count += 1

                if x+1 < W:
                    if maps[y][x+1]=="#":
                        count += 1     

                if y+1 < H:
                    if maps[y+1][x]=="#":
                        count += 1     

                if x-1 >= 0:
                    if maps[y][x-1]=="#":
                        count += 1     


                if y-1 >= 0:
                    if maps[y-1][x]=="#":
                        count += 1     

                if count==1:
                    return "No"
    return "Yes"

ans = solve(W,H,maps)
print(ans)