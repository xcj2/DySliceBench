s = input()
t = input()


def lcs(s, t)->list:
    sn = len(s)
    tn = len(t)
    dp = [[0 for _ in range(tn+1)] for _ in range(sn+1)]
    for i in range(sn):
        for j in range(tn):
            if s[i] == t[j]: dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
            else: dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    #[print(val) for val in dp]
    return dp


def restore_str(lcs_dp)->str:
    restore = str()
    i = len(s)
    j = len(t)

    while i > 0 and j > 0:
        #print(i, j, restore, lcs_dp[i])
        if lcs_dp[i][j] == lcs_dp[i-1][j]: i -= 1
        elif lcs_dp[i][j] == lcs_dp[i][j-1]: j -= 1
        else: 
            restore = s[i-1] + restore
            i -= 1
            j -= 1

    return restore


def main():
    lcs_dp = lcs(s, t)
    ans = restore_str(lcs_dp)
    return print(ans)


if __name__ == '__main__':
    main()