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
    N, _, W = LI()
    a = LI()

    # 初手でラストまで取るとき
    res = abs(a[-1] - W)
    if N == 1:
        print(res)
        return
    res2 = abs(a[-1] - a[-2])

    # 最後から n 枚目を取るときの max, min
    max_li = [0, res, res2] + [0 for _ in range(N)]
    min_li = [INF, res, res2] + [INF for _ in range(N)]
    for i in range(3, N+1):
        take_all = abs(a[-i] - a[-1])
        max_li[i] = min([min_li[j] for j in range(2, i)]+[take_all])
        min_li[i] = max([max_li[j] for j in range(2, i)]+[take_all])

    print(max(max_li))


main()