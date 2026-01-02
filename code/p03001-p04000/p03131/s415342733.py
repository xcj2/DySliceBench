from sys import stderr, setrecursionlimit, exit
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

k,a,b = getInts()

# a>bならひたすら叩くしかない
if a > b:
    print(1+k)
    exit()
# お金を使う操作は順不同なので最後にやってしまって良い
# a枚払ってb枚もらう操作は2回かかるので、差分(b-a)が2枚以下なら2回ポケットを叩くほうが良い
if b - a <= 2 :
    print(1+k)
    exit()

# 初回の交換にかかる回数
k -= a - 1
ans = a

ans += (k//2)*(b-a)
ans += k%2
print(ans)
