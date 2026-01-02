#coding:utf-8
import sys
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = lambda *something : print(*something) if DEBUG else 0
DEBUG = False
def main(given = sys.stdin.readline):
    input = lambda : given().rstrip()
    LMIIS = lambda : list(map(int,input().split()))
    II = lambda : int(input())
    XLMIIS = lambda x : [LMIIS() for _ in range(x)]
    MOD = 10**9+7

    H,W = LMIIS()
    S = [input() for _ in range(H)]
    # print(S)

    def tansaku(S,V,y,x,length):

        
        if  x >= 1 and S[y][x-1] == '.' and V[y][x-1] > length+1:
            V[y][x-1] = length+1
            tansaku(S,V,y,x-1,length+1)


        if x < W-1 and S[y][x+1] == '.' and V[y][x+1] > length+1:
            V[y][x+1] = length+1
            tansaku(S,V,y,x+1,length+1)


        if y >= 1 and S[y-1][x] == '.' and V[y-1][x] > length+1:
            V[y-1][x] = length+1
            tansaku(S,V,y-1,x,length+1)


        if y < H-1 and S[y+1][x] == '.' and V[y+1][x]> length+1:
            V[y+1][x] = length+1
            tansaku(S,V,y+1,x,length+1)

        return
    
    def getmax():
        max_length = 0
        for h in range(H):
            for w in range(W):
                V = [[MOD] * W for _ in range(H)]
                if S[h][w] == '.':
                    V[h][w] = 0
                    tansaku(S,V,h,w,0) 
                for v in V:
                    v = list(map(lambda x:x%MOD,v))
                    max_length = max(v+[max_length])
                    # print(V)
        return max_length
    
    print(getmax())
    






if __name__ == '__main__':
    main()