import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

def main():
    N = ii()
    a,g,c,t=0,1,2,3
    MOD = 10**9+7

    dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(110)]

    def ok(j,k,l):
        f = True
        for x,y,z in [(j,k,l),(j,l,k),(k,j,l)]:
            f = f and not (x == a and y == g and z == c)
        return f


    for j in range(4):
        for k in range(4):
            for l in range(4):
                if not ok(j,k,l): continue
                dp[3][j][k][l] = 1
    
    ans = 0
    for i in range(3,N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for c_char in range(4):
                        if not ok(k,l,c_char): continue
                        elif j == a and c_char == c and (k == g or l == g): continue
                        dp[i+1][k][l][c_char] += dp[i][j][k][l] % MOD

    # print(dp)
    for j in range(4):
            for k in range(4):
                for l in range(4): 
                    ans += dp[N][j][k][l]  % MOD


    print(ans % MOD)



if __name__ == "__main__":
    main()