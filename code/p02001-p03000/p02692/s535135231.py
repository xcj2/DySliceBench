def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

from collections import defaultdict, Counter
from sys import exit
import math
# def seni(dp, a)


def main():
    n, a, b, c = getList()
    a = min(a,2)
    b = min(b, 2)
    c = min(c, 2)
    dp = [[0 for i in range(28)] for j in range(n+1)]
    dp[0][a*9 + b * 3 + c] = 1
    for i in range(n):
        q = input().strip()
        if q == "AB":
            # A->B
            for na in range(1, 3):
                for nb in range(3):
                    for nc in range(3):
                        if dp[i][na * 9 + nb * 3 + nc] != 0:
                            dp[i+1][(na-1) * 9 + min(nb+1, 2) * 3 + nc] = ["AB", na * 9 + nb * 3 + nc]

            for nb in range(1, 3):
                for na in range(3):
                    for nc in range(3):
                        if dp[i][na * 9 + nb * 3 + nc] != 0:
                            dp[i+1][min(na+1, 2) * 9 + (nb-1) * 3 + nc] = ["BA", na * 9 + nb * 3 + nc]

        if q == "BC":
            # B C
            for nb in range(1, 3):
                for na in range(3):
                    for nc in range(3):
                        if dp[i][na * 9 + nb * 3 + nc] != 0:
                            dp[i+1][na * 9 + (nb-1) * 3 + min(nc+1, 2)] = ["BC", na * 9 + nb * 3 + nc]

            for nc in range(1, 3):
                for na in range(3):
                    for nb in range(3):
                        if dp[i][na * 9 + nb * 3 + nc] != 0:
                            dp[i+1][na * 9 + min(nb+1, 2) * 3 + nc-1] = ["CB", na * 9 + nb * 3 + nc]

        if q == "AC":
            # A C
            for na in range(1, 3):
                for nb in range(3):
                    for nc in range(3):
                        if dp[i][na * 9 + nb * 3 + nc] != 0:
                            dp[i+1][(na-1) * 9 + nb * 3 + min(nc + 1, 2)] = ["AC", na * 9 + nb * 3 + nc]

            for nc in range(1, 3):
                for na in range(3):
                    for nb in range(3):
                        if dp[i][na * 9 + nb * 3 + nc] != 0:
                            dp[i+1][min(na+1, 2) * 9 + nb * 3 + nc - 1] = ["CA", na * 9 + nb * 3 + nc]


    # for d in dp:
    #     print(d)

    for i, tgt in enumerate(dp[-1]):
        if tgt != 0:
            ans = hukugen(dp, i, n)
            print("Yes")
            for an in ans:
                print(an)

            return


    print("No")

def hukugen(dp, cur, n):
    ans = []
    taiou = {"A": 9, "B": 3, "C":1}
    for i in range(n):
        moji = dp[n-i][cur][0]
        # print(moji, dp[n-i], cur)
        ans.append(moji[1])
        cur =dp[n-i][cur][1]
        # cur -= taiou[moji[1]]

    return (list(reversed(ans)))


if __name__ == "__main__":
    main()