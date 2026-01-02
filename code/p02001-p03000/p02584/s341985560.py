
def main():
    X, K, D = map(int, input().split())

    if X < 0:
        X = -X
    #Xは正の数
    #min abs(X-kD) ただし k = K-2n

    def f(n: int):
        k = K - 2*n
        return X-k*D

    def is_ok(arg):
        #print("n=", arg)
    # 条件を満たすかどうか？問題ごとに定義
        if f(arg) >= 0:
            return True
        else:
            return False

    def meguru_bisect(ng, ok):
        '''
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng ok は  とり得る最小の値-1 とり得る最大の値+1
        最大最小が逆の場合はよしなにひっくり返す
        '''
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    n = meguru_bisect(0, K//2)
    
    ans = min(abs(f(max(0, n-1))),
        abs(f(n)),
        abs(f(min(K//2+1, n+1)))
    )
    print(ans)

if __name__ == "__main__":
    main()