import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    n,k=map(int,input().split())
    A=sorted(list(map(int,input().split())))
    F=sorted(list(map(int,input().split())),reverse=True)

    # https://qiita.com/drken/items/97e37dd6143e33a64c8c#3-%E3%82%81%E3%81%90%E3%82%8B%E5%BC%8F%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2%E3%81%AE%E3%81%95%E3%82%89%E3%81%AA%E3%82%8B%E5%88%A9%E7%82%B9
    def is_ok(ind):
        cnt=0
        for i in range(n):
            target=ind//F[i]
            if target<A[i]:
                cnt+=A[i]-target
        if cnt<=k:
            return True
        else: return False

    def bin_search_meguru():
        """
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng, okは,とり得る最小の値-1,とり得る最大の値+1
        """
    
        # 適当にいじる
        ng = -1  # ind=0が条件を満たすこともあるため
        ok = A[-1]*F[0]+1  # ind=len(a)-1が条件を満たさないこともあるため
    
        # いじらない
        # okとngのどちらが大きいかわからないことを考慮
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    val=bin_search_meguru()
    print(val)



    
    
resolve()