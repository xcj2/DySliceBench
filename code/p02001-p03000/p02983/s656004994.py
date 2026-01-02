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
    # 2019 = 3* 673
    L, R = LI()

    if (R//673 - (L-1)//673 > 0) and (R//3 - (L-1)//3 > 0):  # 範囲内に 673の倍数も3の倍数もある。
        print(0)
        return
    else: # 範囲は 673 よりも狭いので全探索してもいける。
        minimum = INF
        import itertools
        for x, y in itertools.combinations(range(L, R+1), 2):
            minimum = min((x*y)%2019, minimum)
        print(minimum)
        return


main()