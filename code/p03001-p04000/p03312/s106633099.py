def makelist(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]


N = int(input())
A = [0] + list(map(int, input().split()))


def check(mid, base): # b is max-value
    if mid < base:
        l = imos[mid-1]
        r = imos[base-1] - imos[mid-1]
        return abs(r-l)
    else:
        l = imos[mid] - imos[base-1]
        r = imos[N] - imos[mid]
        return abs(r-l)
        
        

def ternarySearchInt(small, big, i):
    # 初期条件
    if small == big:
        return small
    elif big - small == 1:
        if check(small, i) <= check(big, i):
            return small
        else:
            return big

    def func(small, big):
        midl = (big + small) // 2
        midr = midl + 1
        if big - small == 2:  # 終了条件
            mid = midl
            if check(small, i) <= check(mid, i):
                if check(small, i) <= check(big, i):
                    return small
                else:
                    return big
            else:
                if check(mid, i) <= check(big, i):
                    return mid
                else:
                    return big
        else:
            if check(midl, i) > check(midr, i):
                return func(midl, big)
            else:
                return func(small, midr)
    return func(small, big)



imos = [0]*(N+1)
for i in range(1, N+1):
    imos[i] = imos[i-1] + A[i]

ans = int(1e18)
for i in range(3, N):
    l = ternarySearchInt(1, i-1, i)
    r = ternarySearchInt(i, N, i)
    P = imos[l-1]
    Q = imos[i-1] - P
    R = imos[r] - imos[i-1]
    S = imos[N] - imos[r]
    hoge = [P,Q,R,S]
    ans = min(ans, max(hoge) - min(hoge))


print(ans)

