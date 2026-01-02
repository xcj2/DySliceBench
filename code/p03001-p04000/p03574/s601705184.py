def nyu():
    H,W = map(int,input().split())
    S = [list(input()) for i in range(H)] 
    return S,H,W

def check(S,H,W):

    for h in range(H):
        for w in range(W):
            if S[h][w] != "#":
                if h !=0 :
                    if S[h-1][w] == "#":
                        S[h][w] +=1
                if h !=H-1 :
                    if S[h+1][w] == "#":
                        S[h][w] +=1
                if w !=0 :
                    if S[h][w-1] == "#":
                        S[h][w] +=1
                if w !=W-1 :
                    if S[h][w+1] == "#":
                        S[h][w] +=1
#右斜め
                if h !=H-1  and w !=W-1:                    
                    if S[h+1][w+1] == "#":
                        S[h][w] +=1
                if h != 0  and w !=W-1:                    
                    if S[h-1][w+1] == "#":
                        S[h][w] +=1
#左斜め下　左斜め上
                if h !=H-1  and w !=0:                    
                    if S[h+1][w-1] == "#":
                        S[h][w] +=1

                if h != 0  and w !=0:                    
                    if S[h-1][w-1] == "#":
                        S[h][w] +=1

    for a in S:
       print(*a,sep='')
 

def convert(S,H,W):
    
    for h in range(H):
        for w in range(W):
            if S[h][w]==".":
                S[h][w] = 0
    return S

S,H,W = nyu()
S =convert(S,H,W)
check(S,H,W)
