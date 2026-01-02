border = 101


def manhattan_distance(Cx, Cy, H, X, Y):
    return max(H - abs(X - Cx) - abs(Y - Cy), 0)


def judge_center(Cx, Cy, cords):
    for x, y, h in cords:
        if h > 0:
            H = abs(x - Cx) + abs(y - Cy) + h
            break
    for x, y, h in cords:
        tmp = manhattan_distance(Cx, Cy, H, x, y)
        if h != tmp:
            return -1
    return H


def main():
    N = int(input())
    cords = [list(map(int, input().split(' '))) for _ in range(N)]

    for tmp_Cx in range(border):
        for tmp_Cy in range(border):
            h = judge_center(tmp_Cx, tmp_Cy, cords)
            if h != -1:
                print('{} {} {}'.format(tmp_Cx, tmp_Cy, h))
                return 0


if __name__ == '__main__':
    main()
