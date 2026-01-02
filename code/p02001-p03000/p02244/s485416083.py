import copy as cp
N = 8
ans = []

def out(M):
    for i in range(N):
        for j in range(N):
            print(M[i][j], end="")
        print("")
    
def DFS(r,c,dp,dn,qn):
    global ans
    if qn == N:
        for h in range(N):
            for w in range(N):
                if r[h] & c[w] & dp[h+w] & dn[w-h+7]:
                    ans.append([h,w])
                    return True
        return False

    for h in range(N):
        for w in range(N):
            if r[h] & c[w] & dp[h+w] & dn[w-h+7]:
                new_r = cp.deepcopy(r)
                new_c = cp.deepcopy(c)
                new_dp = cp.deepcopy(dp)
                new_dn = cp.deepcopy(dn)
                new_r[h],new_c[w],new_dp[h+w],new_dn[w-h+7] = False,False,False,False
                if DFS(new_r,new_c,new_dp,new_dn,qn+1):
                    ans.append([h,w])
                    return True
    return False


def main():
    row = [True]*N
    col = [True]*N
    dp = [True]*(2*N-1)
    dn = [True]*(2*N-1)
    k = int(input())
    MAP = [["." for _ in range(N)] for __ in range(N)]
    for _ in range(k):
        h,w = map(int,input().split())
        MAP[h][w] = "Q"
        row[h] = False
        col[w] = False
        dp[w+h] = False
        dn[w-h+7] = False
    
    DFS(row,col,dp,dn,k+1)

    
    for h,w in ans:
        MAP[h][w] = "Q"

    out(MAP)

main()

