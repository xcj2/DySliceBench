import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():


    s = "#" + S()
    t = "#" + S()

    dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]

    for i in range(len(t)-1):
        for j in range(len(s)-1):
            if t[i+1] == s[j+1]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])


    ans = ""
    now = dp[len(t)-1][len(s)-1]
    zahyo = [len(t)-1, len(s)-1]
    while now != 0:
        while dp[zahyo[0]][zahyo[1]-1]==now:
            zahyo[1]-=1
        while dp[zahyo[0]-1][zahyo[1]]==now:
            zahyo[0]-=1

        ans += t[zahyo[0]]

        now -= 1
        zahyo = [zahyo[0]-1, zahyo[1]-1]

    ans = ans[::-1]

    print(ans)

main()
