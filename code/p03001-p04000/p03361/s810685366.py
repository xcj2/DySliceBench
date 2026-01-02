def makegrid(target=False):
    H,W = map(int,input().split())
    S = [["" for i in range(W+2)]for j in range(H+2)]
    target_xy = []
    for y in range(H):
        line = input()
        for x in range(W):
            S[y+1][x+1] = line[x]
            if line[x] == target:
                target_xy.append([y+1,x+1])
    return H,W,S,target_xy

def getvalue_9(S,y,x): 
    around9 = [None for i in range(9)]      
    idx = 0 
    for h in range(-1,2):
        for w in range(-1,2):
            around9[idx] = S[y+h][x+w]
            idx +=1
    return around9

def getvalue_4(S,y,x):
    around4 = [S[y+1][x],S[y][x-1],S[y][x+1],S[y-1][x]]
    return around4

H,W,S,targets_xy = makegrid(target="#")
ans = "Yes"
for xy in targets_xy:
    around4 = getvalue_4(S,xy[0],xy[1])
    if not ("#" in around4):
        ans = "No"

print(ans)