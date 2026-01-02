import sys

sys.setrecursionlimit(10 ** 7)
debug = True

debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def matdprint(mat):
    if debug == True:
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                print(mat[i][j], end=', ')
            print()

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()

INF = 10 ** 18
MOD = 10 ** 9 + 7
def conv(s):
    cnt = 0
    for n in s:
        cnt += 2**n
    return cnt

def main():

    N, M = LI()

    a_list = []
    b_list = []
    c_list = []
    for i in range(M):
        a, b = LI()
        a_list.append(a)
        # b_list.append(b)
        c_list.append(LI())

    dp = [[0 for j in range(2**N)]for i in range(M)]

    def conv(c):
        key = 0
        for i in c:
            key += 2**(i-1)
        return key

    def update(i, j, a):
        if dp[i][j] == 0:
            dp[i][j] = a
        else:
            dp[i][j] = min(dp[i][j], a)

    for i in range(M):
        c = c_list[i]
        a = a_list[i]
        key = conv(c)
        dprint('i', i, 'a', a, 'key', key)

        # 無に自分を入れるパターン
        if dp[i - 1][key] != 0:
            dp[i][key] = min(dp[i - 1][key], a)
        else:
            dp[i][key] = a


        for j in range(2**N):
            org_key = j
            or_key = j | key

            # 直前パターンに自分を足す場合
            # if dp[i-1][org_key] == 0:
            #     # 直前orgがなければ足せない
            #     # dprint('org_key', org_key, 'or_key', or_key, 'pass')
            # else:
            if dp[i - 1][org_key] != 0:

                # 直前がある場合、直前orgに足したのを入れる
                update(i, or_key, dp[i-1][org_key] + a)

                # dprint('org_key', org_key, 'or_key', or_key, dp[i][or_key])

            # 直前パターンをすべて引き継がせる
            if dp[i-1][j] != 0:
                update(i, j, dp[i-1][j])

        # matdprint(dp)

    # matdprint(dp)
    ans = dp[M-1][(2**N)-1]
    if ans == 0:
        print(-1)
    else:
        print(ans)

main()