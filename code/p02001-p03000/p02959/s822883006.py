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

debug = True
#debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def solve():
    N = II()
    a_list = LI()
    b_list = LI()

    ans = 0
    left = a_list[0]

    for i in range(N):
        power = b_list[i]
        if power >= left:
            # 左をすべて倒せる
            ans += left
            power = power - left
        else:
            # 左をすべて倒せない
            ans += power
            power = 0

        right = a_list[i+1]
        if power >= right:
            # 右をすべて倒せる
            ans += right
            left = 0 # 次の勇者のleftは0
        else:
            # 右が余るとき
            ans += power
            left = right - power # 次の勇者にはあまりがある

    print(ans)
solve()