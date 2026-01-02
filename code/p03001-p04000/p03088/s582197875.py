#!/usr/bin/env py

log = lambda *x: print(*x)

def no_c(f,s,t):
    if f==1 and t==2: return True
    if f==1 and s==2: return True
    if s==1 and t==2: return True
    if s==2 and t==1: return True
    return False

def no_g(f,s,t):
    if s==1 and t==3: return True
    return False

def solve(k):
    dp = [[ [([0]*5) for i in range(5)] for i in range(5) ] for i in range(k+1)]

    for l in range(k, 0, -1):
        for f in range(0,5):
            for s in range(0,5):
                for t in range(0,5):
                    if l == k:
                        dp[l][f][s][t] = 1
                        continue

                    if l == 1:
                        dp[l][f][s][t] = dp[l+1][s][t][1] + dp[l+1][s][t][2] + dp[l+1][s][t][3] + dp[l+1][s][t][4]

                    if l == 2:
                        if (s==1 and t==2) or (s==2 and t==1): dp[l][f][s][t] = dp[l+1][s][t][1] + dp[l+1][s][t][2] + dp[l+1][s][t][4]
                        if (s==1 and t==3): dp[l][f][s][t] = dp[l+1][s][t][1] + dp[l+1][s][t][3] + dp[l+1][s][t][4]
                        else: dp[l][f][s][t] = dp[l+1][s][t][1] + dp[l+1][s][t][2] + dp[l+1][s][t][3] + dp[l+1][s][t][4]

                    if no_c(f,s,t): dp[l][f][s][t] = dp[l+1][s][t][1] + dp[l+1][s][t][2] + dp[l+1][s][t][4]
                    elif no_g(f,s,t): dp[l][f][s][t] = dp[l+1][s][t][1] + dp[l+1][s][t][3] + dp[l+1][s][t][4]
                    else: dp[l][f][s][t] = dp[l+1][s][t][1] + dp[l+1][s][t][2] + dp[l+1][s][t][3] + dp[l+1][s][t][4]

    return sum(dp[1][0][0][t] for t in (1,2,3,4)) % 1000000007

log(solve(int(input())))
