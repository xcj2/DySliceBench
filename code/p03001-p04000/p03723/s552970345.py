'''
https://youtu.be/UHfTqvaD0pk?t=22m58s
なぜ、操作がすぐ終わるのか
1stepごとに最大と最小の差が半分になるため

aa bb cc: aa最小, cc最大, 差は2(c-a)
bc ac ab: ab最小, bc最大, 差は(c-a) <- 半分!!

https://qiita.com/7shi/items/41d262ca11ea16d85abc#%E3%83%93%E3%83%83%E3%83%88%E3%81%AE%E5%90%88%E6%88%90
ビットの合成
'''

def iin(): return int(input())
def nl(): return list(map(int, input().split()))

def func(x, y, z):
    if (x | y | z) & 1:#どれかが奇数ならTrue
        return 0
    if (x == y) and (x == z):
        return -1

    #x, y, zは全て偶数なので、/ではなく//で問題ない
    x2 = (y + z) // 2
    y2 = (x + z) // 2
    z2 =  (x + y) // 2

    return func(x2, y2, z2) + 1

a, b, c = nl()
print(func(a, b, c))