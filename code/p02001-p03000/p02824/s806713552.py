import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,M,V,P = MI()
A = [0] + LI()
A.sort()

from bisect import bisect_left


def f(n):  # 下からn番目のスコアの問題が、採用される可能性があるか
    v = V-n  # スコア下位n問には全員が投票したとしてよい
    if A[n] + M < A[-P]:  # 上位P人に入れない
        return False
    else:
        v -= P-1  # スコア上位P-1人には全員が投票したとしてよい
        if v <= 0:
            return True
        else:
            if sum(A[n]+M-A[i] for i in range(n+1,N-P+2)) >= M*v:
                return True
            else:
                return False


left = 0  # 採用される可能性なし
right = N  # 採用される可能性あり
while left + 1 < right:
    mid = (left + right)//2
    if f(mid):
        right = mid
    else:
        left = mid

print(N+1-right)
