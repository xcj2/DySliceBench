import sys

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

def main():
    h, n = LI()
    a_s = []
    b_s = []

    for i in range(n):
        a, b = LI()
        a_s.append(a)
        b_s.append(b)

    dp = [INF for j in range(h+1)]
    dp[0] = 0
    for i in range(h):
        for j in range(n):
            if i + a_s[j] > h:
                if dp[h] > dp[i] + b_s[j]:
                    dp[h] = dp[i] + b_s[j]
            else:
                if dp[i + a_s[j]] > dp[i] + b_s[j]:
                    dp[i + a_s[j]] = dp[i] + b_s[j]

    print(dp[h])

if __name__ == '__main__':
    main()