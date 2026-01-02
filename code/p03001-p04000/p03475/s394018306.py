from sys import stderr, setrecursionlimit
from math import ceil
setrecursionlimit(2147483647)
def getInt():
    return int(input())
def getInts():
    return [int(i) for i in input().split()]
def getIntLines(n=1):
    res = []
    for _ in range(n):
        res.append(getInt())
    return res
def getIntsLines(n=1):
    res = []
    for _ in range(n):
        res.append(getInts())
    return res
def debug(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

n = getInt()
ans = []
for i in range(n-1):
    c, s, f = getInts()
    ans.append(c + s)
    for j in range(i):
        # ans[j]にはj駅からi駅にたどり着くまでの最短時間が入っている
        if ans[j] <= s:
            # 最初の出発時間より速く到達できれば律速はi駅の最初の出発時間になる
            ans[j] = ans[i]
        else:
            # 最初の電車に乗れなかった場合，(ans[j]より大きい最小のfの倍数)時間まで待つ必要がある(さらに電車に乗る時間cを加える)
            # min({x | x % f == 0, x > ans[j]})
            ans[j] = ceil(ans[j]/f) * f + c
    debug(ans)

print(*ans, sep='\n')
print(0)
