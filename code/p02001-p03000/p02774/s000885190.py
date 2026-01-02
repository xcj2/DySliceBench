
from bisect import bisect_left, bisect_right
def resolve():
    def judge_m(mid):
        tot = 0
        for i in range(p_n):
            d = mid//P[i]
            tot += bisect_right(M, d)
        return tot >= K


    def judge_p(mid):
        tot = 0
        for i in range(p_n): # 正と正の積
            d = mid//P[i]
            tmp = bisect_right(P, d)
            if i < tmp:
                tmp -= 1 # 自身を除く
            tot += tmp
        for i in range(m_n): # 負と負の積
            d = mid//M[i]
            tmp = bisect_right(M, d)
            if i < tmp:
                tmp -= 1 # 自身を除く
            tot += tmp
        tot //= 2
        return tot >= K


    INF = 10 ** 18 + 1
    N, K = map(int, input().split())
    A = sorted(map(int, input().split()))

    P = []
    M = []
    Z = []
    for a in A:
        if a > 0:
            P.append(a)
        elif a < 0:
            M.append(a)
        else:
            Z.append(a)

    p_n = len(P)
    m_n = len(M)
    z_n = len(Z)
    minus = p_n * m_n
    zero = z_n*(z_n-1)//2 + z_n*p_n + z_n*m_n
    plus = p_n*(p_n - 1)//2 + m_n*(m_n-1)//2

    if K <= minus: # X が負の時
        M.sort()
        l, u = -INF, 0
        while u - l > 1:
            mid = (u+l)//2
            if judge_m(mid):
                u = mid
            else:
                l = mid
        return print(u)
    elif K <= (minus + zero):
        return print(0)
    elif K <= (minus + zero + plus):
        K -= (minus + zero)
        M = [abs(m) for m in M]
        P.sort()
        M.sort()
        l, u = -1, INF
        while u - l > 1:
            mid = (u + l)//2
            if judge_p(mid):
                u = mid
            else:
                l = mid
        return print(u)


if __name__ == "__main__":
    resolve()
