# 税抜価格から税込価格を計算する関数
#
#  [引数]
#   zeinuki  : 税抜価格(整数)
#   zeiritsu : 税率(パーセント, 整数)
#  [返り値]
#   税込価格(整数)
def calcZeikomi(zeinuki, zeiritsu):
    return zeinuki + zeinuki * zeiritsu // 100

# 税込価格から税抜価格の最小値を探索する関数
#
# [考え方]
#  税抜価格の最小値は1から税込価格の間にあり、1から探索すれば最小値が求まる
# [引数]
#  zeikomi  : 税込価格(整数)
#  zeiritsu : 税率(パーセント, 整数)
# [返り値]
#  税抜価格の最小値(整数)。存在しない場合はNone。
def calcZeinukiMinimum(zeikomi, zeiritsu):
    for i in range(1, zeikomi + 1):
        if (calcZeikomi(i, zeiritsu) == zeikomi):
            return i
    return None

# 税込価格から税抜価格の最大値を探索する関数
#
# [考え方]
#  税抜価格の最大値は1から税込価格の間にあり、税込価格から探索すれば最大値が
#  求まる
# [引数]
#  zeikomi  : 税込価格(整数)
#  zeiritsu : 税率(パーセント, 整数)
# [返り値]
#  税抜価格の最大値(整数)。存在しない場合はNone。
def calcZeinukiMaximum(zeikomi, zeiritsu):
    for i in range(zeikomi, 0, -1):
        if (calcZeikomi(i, zeiritsu) == zeikomi):
            return i
    return None

# 改定価格の最大値を計算する関数
#
# [引数]
#  rate0  : 変更前の消費税率(整数)
#  rate1  : 変更後の消費税率(整数)
#  price0 : 消費税率変更前の価格(整数)
# [返り値]
#  消費税率変更後の価格(整数)。存在しなければNone。
def calcKaiteiMaximum(rate0, rate1, price0):
    zeinuki = calcZeinukiMaximum(price0, rate0)
    if (zeinuki == None):
        return None
    return calcZeikomi(zeinuki, rate1)

# 問題を解く関数
#
# [考え方]
#  2商品の合計価格が与えられるので、総当たり法を実施
# [引数]
#  x : 変更前の消費税率(パーセント, 整数)
#  y : 変更後の消費税率(パーセント, 整数)
#  s : 消費税率変更前の２商品の税込合計価格
def solve(x, y, s):
    res = 0
    for i in range(1, s):
        price1 = calcKaiteiMaximum(x, y, i)
        price2 = calcKaiteiMaximum(x, y, s - i)
        if (price1 == None or price2 == None):
            continue
        res = max(res, price1 + price2)
    return res

# メインルーチン
while (True):
    ary = input().split()
    x = int(ary[0])
    y = int(ary[1])
    s = int(ary[2])
    if (x == 0 and y == 0 and s == 0):
        break
    print(solve(x, y, s))
