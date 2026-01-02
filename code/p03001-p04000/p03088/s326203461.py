def dynamic_programming(N):
    mod = 10 ** 9 + 7
    dp = [{} for _ in range(N+1)] 
    dp[0]['TTT'] = 1
    for n in range(N):
        for last3 in dp[n].keys():
            for c in 'ACTG':
                if is_ok(last3 + c):
                    if last3[1:] + c in dp[n+1].keys():
                        dp[n+1][last3[1:] + c] += dp[n][last3] % mod
                    else:
                        dp[n+1][last3[1:] + c] = dp[n][last3] % mod
    ret = sum(dp[N].values()) % mod
    return ret

def is_ok(last4):
        
    for i in range(4):
        t = list(last4)
        if i < 3:
            t[i], t[i+1] = t[i+1], t[i]
        if ''.join(t).count('AGC') > 0:
            return False
    return True

def main():

    n = int(input())
    #solver = DP(n)

    #print(solver.dp(0, 'CCC'))
    print(dynamic_programming(n))


main()