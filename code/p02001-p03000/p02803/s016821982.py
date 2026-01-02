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


    H,W = LMIIS()
    MOD = H*W
    S = [input() for _ in range(H)]

    from collections import deque
    def tansaku(S,V,length,q):
        if len(q) == 0:
            return length-1
        q2 = []
        for y,x in q:
            if  x >= 1 and S[y][x-1] == '.' and V[y][x-1]:
                V[y][x-1] = False
                q2.append((y,x-1))

            if x < W-1 and S[y][x+1] == '.' and V[y][x+1]:
                V[y][x+1] = False
                q2.append((y,x+1))

            if y >= 1 and S[y-1][x] == '.' and V[y-1][x]:
                V[y-1][x] = False
                q2.append((y-1,x))

            if y < H-1 and S[y+1][x] == '.' and V[y+1][x]:
                V[y+1][x] = False
                q2.append((y+1,x))

        return tansaku(S,V,length+1,q2)
    
    def getmax():
        max_length = 0
        for h in range(H):
            for w in range(W):
                V = [[True] * W for _ in range(H)]
                if S[h][w] == '.':
                    V[h][w] = False
                    max_length = max(tansaku(S,V,0,[(h,w)]),max_length)
        return max_length
    
    print(getmax())
   
    






if __name__ == '__main__':
    main()