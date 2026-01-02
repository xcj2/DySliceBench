import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main():
    s = SI()
    t = SI()

    # そこまでの最大の長さ
    dp_table_2 = [[0 for _ in range(len(s))] for _ in range(len(t))]
    # init:
    ume = 0
    for i in range(len(s)):
        if t[0] == s[i]:
            ume = 1
        dp_table_2[0][i] = ume
    ume = 0
    for i in range(len(t)):
        if t[i] == s[0]:
            ume = 1
        dp_table_2[i][0] = ume

    # dp:
    for i in range(1, len(t)):
        for j in range(1, len(s)):
            if t[i] == s[j]:
                dp_table_2[i][j] = max(dp_table_2[i-1][j], dp_table_2[i][j-1], dp_table_2[i-1][j-1]+1)
            else:
                dp_table_2[i][j] = max(dp_table_2[i-1][j], dp_table_2[i][j-1])

    # print(dp_table_2)

    # print(dp_table_2[len(t)-1][len(s)-1])

    # 復元
    i = len(t) - 1
    j = len(s) - 1
    ans = ''
    while i >= 0 and j >= 0:
        if i == 0 and j == 0:
            if dp_table_2[0][0] > 0:
                ans += s[0]
            break
        if j == 0:
            if dp_table_2[i][j] != dp_table_2[i-1][j]:
                ans += t[i]
            i -= 1
            continue
        if i == 0:
            if dp_table_2[i][j] != dp_table_2[i][j-1]:
                ans += s[j]
            j -= 1
            continue
        if dp_table_2[i][j] != dp_table_2[i][j-1] and dp_table_2[i][j] != dp_table_2[i-1][j]:
            ans += t[i]
            i -= 1
            j -= 1
        elif dp_table_2[i][j] != dp_table_2[i][j-1]: 
            i -= 1
        elif dp_table_2[i][j] != dp_table_2[i-1][j]: 
            j -= 1
        else:
            j -= 1

    print(ans[::-1])

main()