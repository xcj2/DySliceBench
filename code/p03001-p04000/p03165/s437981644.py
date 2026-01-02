import sys
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template

# BEGIN CUT HERE
def lcs(s, t):
    '''s,tは文字列をリスト化したもの'''
    n = len(s)
    m = len(t)
    s.append('$')
    t.append('%')
    dp = [[0 for _j in range(m + 2)] for _i in range(n + 2)]
    dp[0][0] = 0
    for i in range(n+1):
        for j in range(m+1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (s[i] == t[j]))
    # return dp[n][m]
    '''復元する'''
    length = dp[n][m]
    ans = ['']*(length+1)
    while(length > 0):
        if(s[n] == t[m]):
            ans[length] = s[n]
            n-=1
            m-=1
            length-=1
        elif(dp[n+1][m+1] == dp[n][m+1]):
            n-=1
        else:
            m-=1
    return ''.join(ans[1:])
# END CUT HERE

def ALDS1_10_C():
    q = ii()
    for _ in range(q):
        s = li()
        t = li()
        print(lcs(s, t))

def EDPC_F():
    s = li()
    t = li()
    print(lcs(s,t))


if __name__ == '__main__':
    # ALDS1_10_C()
    EDPC_F()