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
    N, W = LI()
    wv = []
    for _ in range(N):
        wv.append(LI())


    # 横軸 v, 縦軸 n
    dp_table = [[None for _ in range(10**5+1)] for _ in range(N)]
    
    # init
    w0, v0 = wv[0]
    dp_table[0][0] = 0
    dp_table[0][v0] = w0

    # dp
    for i, item in enumerate(wv):
        if i== 0: continue
        w,v = item
        for val, weight in enumerate(dp_table[i-1]):
            if weight is not None:
                # i番目の荷物を入れないとき
                dp_table[i][val] = min(dp_table[i][val], weight) if dp_table[i][val] is not None else weight
                # i番目の荷物を入れるとき
                dp_table[i][val+v] = weight + w

    v  = 10**5
    for w in reversed(dp_table[N-1]):
        if w and w <= W:
            print(v)
            break
        v -= 1


main()