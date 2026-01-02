import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

class Solver(object):
    def __init__(self):
        pass

    def solve(self,s:str,t:str) -> int:
        ## DP loop
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+1)
                dp[i+1][j+1] = max(dp[i+1][j+1],dp[i+1][j],dp[i][j+1])
        
        ans = ""

        ## Recover the LCS from DP table
        ## checking the update point
        l,m = len(s),len(t)
        while l > 0 and m >0:
            if dp[l][m] == dp[l-1][m]:
                l -= 1
            elif dp[l][m] == dp[l][m-1]:
                m -= 1
            else:
                ans = t[m-1] + ans
                l -= 1
                m -= 1

        return ans

def main():
    s = input().rstrip()
    t = input().rstrip()
    solver = Solver()
    print(solver.solve(s,t))

if __name__ == "__main__":
    main()