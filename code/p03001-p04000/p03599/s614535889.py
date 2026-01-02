
import math

def read_input():
    a, b, c, d, e, f = map(int, input().split())
    return a, b, c, d, e, f


# 100aと100bの線形結合でf以下でとりうる値を見つける
def search_water_valiation(a, b, f):
    result = []
    for i in range(30):
        for j in range(30):
            water = 100*a*i + 100*b*j
            if water <= f:
                result.append(water)

    result = list(set(result))
    result.sort()

    return result


# c, dの線形結合でmax_sugar以下の最大値を探す
# cx + dy <= max_sugarより
# y <= - c/d x + max_sugar/d
# xの範囲は(0, max_sugar/c)
def search_most_sweet(c, d, max_sugar):
    sugars = []
    for x in range(math.floor(max_sugar/c) + 1):
        y = math.floor((-c * x + max_sugar)/d)
        sugars.append(c*x + d*y)

    sugars = list(set(sugars))
    return max(sugars)

def submit():
    a, b, c, d, e, f = read_input()

    waters = search_water_valiation(a, b, f)
    max_sugars = [min(w * e // 100, f - w) for w in waters]

    result = []
    for water, max_sugar in zip(waters, max_sugars):
        sugar = search_most_sweet(c, d, max_sugar)
        result.append((water, sugar))

    result = [r for r in result if r[0] + r[1] <= f]
    result = [(w+s, s, 100 * s / (w + s)) for (w, s) in result if (w, s) != (0, 0)]

    r = max(result, key=lambda x:x[2])
    print('{} {}'.format(r[0], r[1]))

if __name__ == '__main__':
    submit()