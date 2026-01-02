
import sys

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7

def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return sys.stdin.readline()[:-1]

def main():
    n = II()
    s = S()
    inf = n + 2
    m = [[0 for i in range(n)] for i in range(n)]
    first = [[inf for i in range(n)] for i in range(n)]
    # set 1st index value
    lcs = 0
    for i, c in enumerate(s):
        # print(c, s[0])
        if c == s[0]:
            m[i][0] = 1
            first[i][0] = i
            if i != 0:
                lcs = 1
    for i in range(1, n):
        for j in range(1, n):
            if i <= j:
                continue
            if s[i] == s[j]:
                if first[i-1][j-1] > j:
                    m[i][j] = m[i-1][j-1] + 1
                    lcs = max(m[i][j], lcs)
                    if first[i-1][j-1] == inf:
                        first[i][j] = i
                    else:
                        first[i][j] = first[i-1][j-1]
            else:
                m[i][j] = 0

    # print(m)
    print(lcs)


if __name__ == '__main__':
    main()