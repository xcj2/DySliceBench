
from itertools import combinations

def read_input():
    d, g = map(int, input().split())

    points = []
    for i in range(d):
        points.append(tuple(map(int, input().split())))

    return d, g, points


def extract(x, lst):
    # xを2進数でlen(lst)桁に変換する
    bin_x = bin(x)[2:]
    bin_x = '0'* (len(lst) - len(bin_x)) + bin_x

    return [l for l, b in zip(lst, bin_x) if b == '1']


def submit():
    d, g, points = read_input()
    points = [(i*100, p, c) for i, (p, c) in enumerate(points, start=1)]

    min_count = float('inf')
    for fp in points:
        # fpを除き、完全に解く問題セットを選ぶ

        rest_points = points.copy()
        rest_points.remove(fp)
        for i in range(2 ** len(rest_points)):
            # コンプする問題を抽出
            comps = extract(i, rest_points)
            solved = 0
            get_points = 0
            for c in comps:
                solved += c[1]
                get_points += c[0] * c[1] + c[2]

            if g > get_points:
                rest = g - get_points
                if rest > fp[0] * fp[1] + fp[2]:
                    # fpだけではgは満たせないので失敗
                    continue
                else:
                    if rest > fp[0] * fp[1]:
                        # ボーナス込みで満たせる
                        solved += fp[1]
                    elif rest % fp[0]:
                        solved += rest // fp[0] + 1
                    else:
                        solved += rest // fp[0]
            
            if min_count > solved:
                min_count = solved

    print(min_count)


if __name__ == "__main__":
    submit()
