import collections, itertools, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N, K = LI()
    xy = [LI() for _ in range(N)]

    # x, y全ての重複あり組み合わせに対して含まれる点の個数を算出する

    x_cnt = collections.Counter([i[0] for i in xy])
    x_coordinate = list(x_cnt.keys())
    x_coordinate.sort()
    # len_x_c = len(x_coordinate)
    y_cnt = collections.Counter([i[1] for i in xy])
    y_coordinate = list(y_cnt.keys())
    y_coordinate.sort()
    len_y_c = len(y_coordinate)

    ans = INF
    for xl, xh in itertools.combinations(x_coordinate, 2):
        # 4番目の辺の探索は、個数条件を満たしたら終了していよい
        for i in range(len_y_c - 1):
            yl = y_coordinate[i]
            for j in range(i + 1, len_y_c):
                yh = y_coordinate[j]
                cnt = len([(i, j) for i, j in xy if xl <= i <= xh and yl <= j <= yh])
                if cnt >= K:
                    ans = min((xh - xl) * (yh - yl), ans)
                    break

    print(ans)

if __name__ == '__main__':
    resolve()
