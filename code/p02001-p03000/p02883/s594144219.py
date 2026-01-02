#ABC144-E Gluttony
"""
消化コストの小さい人から食べにくさの大きいものを割り当てるのは確定。
問題は全員のコスト*食べにくさ　の合計ではなく、最もその値が大きい人の
スコアを最小化することである。

最大値の最小化は、最大値を決め打って二分探索。
コストの昇順と食べにくさの降順を対応させ、食べにくさ*need<=決め打った最大値
となるようなneedを求め、k -= max(0,-need+コスト)していく。
kが0未満になってしまった場合はその決め打った最大値は達成できない。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,k = map(int,readline().split())
lsta = list(map(int,readline().split()))
lstf = list(map(int,readline().split()))

lsta.sort()
lstf.sort(reverse=True)
def func(mid,k):
    for i in range(n):
        need = mid//lstf[i] #need以下にしないといけない
        k -= max(0,lsta[i]-need)
        if k < 0:
            return 0
    return 1

def binary_search(): #2分探索
    ok = 10**20
    ng = -1
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if func(mid,k):
            ok = mid
        else:
            ng = mid

    return ok

print(binary_search())
