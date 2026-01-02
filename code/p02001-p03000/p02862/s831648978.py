import sys

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]


def main():
    def cmb(n, r, MOD):
        if ( r<0 or r>n ):
            return 0
        r = min(r, n-r)
        return g1[n] * g2[r] * g2[n-r] % MOD

    N = 10**6
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル

    for i in range( 2, N + 1 ):
        g1.append( ( g1[-1] * i ) % MOD )
        inverse.append( ( -inverse[MOD % i] * (MOD//i) ) % MOD )
        g2.append( (g2[-1] * inverse[-1]) % MOD )

    x, y = LI()
    if (x + y) % 3 != 0:
        print(0)
        return

    sum_ = (x + y) // 3
    tmp_x = 2 * sum_
    if sum_ > x or sum_ > y:
        print(0)
        return

    if tmp_x > x:
        c_y = tmp_x - x
        c_x = sum_ - c_y
    else:
        c_y = -(tmp_x - x)
        c_x = sum_ - c_y

    print(cmb(sum_, c_x, MOD))


if __name__ == '__main__':
    main()