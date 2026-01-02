def makelist(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]


N = int(input())
A = list(map(int, input().split()))



def check(b):
    res = 0
    for i in range(N):
        res += abs(A[i] - (b+(i+1)))
    #print(b, res)
    return res

def ternarySearchInt(small, big):
    # 初期条件
    if small == big:
        return small
    elif big - small == 1:
        if check(small) <= check(big):
            return small
        else:
            return big

    def func(small, big):
        midl = (big + small) // 2
        midr = midl + 1
        if big - small == 2:  # 終了条件
            mid = midl
            if check(small) <= check(mid):
                if check(small) <= check(big):
                    return small
                else:
                    return big
            else:
                if check(mid) <= check(big):
                    return mid
                else:
                    return big
        else:
            if check(midl) >= check(midr):
                return func(midl, big)
            else:
                return func(small, midr)
    return func(small, big)

ans = ternarySearchInt(-int(1e9), int(1e9))
#print(check(0))
print(check(ans))
