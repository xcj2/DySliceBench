
def read_input():
    n = int(input())
    slist = []
    for i in range(n):
        slist.append(int(input()))
    return n, slist

# return matrix initialized by zero
# shape = (n, m)
def make_2d_matrix(n, m):
    result = []
    for i in range(n):
        result.append([0]*m)

    return result


def submit():
    n, slist = read_input()
    total = sum(slist)
    dp = make_2d_matrix(len(slist) + 1, total + 1)

    # dp[0][0] = 1 , dp[0][not 0] = 0
    # dp[i][j]はi番目のsまででjになる/ならない
    # dp[i][j] =
    #       1 if dp[i - 1][j] == 1
    #       1 if dp[i - 1][j - xj] == 1

    dp[0][0] = 1
    for i in range(1, len(slist) + 1):
        for j in range(total + 1):
            if dp[i - 1][j] == 1:
                dp[i][j] = 1
            else:
                if j - slist[i - 1] >= 0:
                    if dp[i - 1][j - slist[i - 1]] == 1:
                        dp[i][j] = 1

    maxscore = 0
    for s in range(total + 1):
        if dp[len(slist)][s] == 1:
            if s % 10:
                if maxscore < s:
                    maxscore = s

    print(maxscore)


if __name__ == '__main__':
    submit()