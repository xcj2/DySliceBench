

def read_input():
    n = int(input())
    conds = []
    for _ in range(n):
        x, y, h = map(int, input().split())
        conds.append(((x, y), h))

    return n, conds


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def satisfy(cond, center):
    c, ch = center
    p, h = cond
    return ch == h + manhattan(p, c)


def zero_satisfy(cond, center):
    c, ch = center
    p, h = cond
    return ch <= manhattan(p, c)


def submit():
    n, conds = read_input()    

    if n == 1:
        p, h = conds[0]
        print("{} {} {}".format(p[0], p[1], h))
        return

    plus_conds = [c for c in conds if c[1] > 0]
    zero_conds = [c for c in conds if c[1] == 0]
    st = plus_conds[0]

    center_cands = []
    for i in range(101):
        for j in range(101):
            t = (i, j)
            th = st[1] + manhattan(st[0], t) # 仮にtがpより高い位置の頂点だとする
            center_cands.append((t, th))
    
    # 各条件について満たすか否かを判定していく
    for cond in plus_conds[1:]:
        center_cands = [c for c in center_cands if satisfy(cond, c)]

    # h=0の条件について、有効かどうか判定していく
    for cond in zero_conds:
        center_cands = [c for c in center_cands if zero_satisfy(cond, c)]

    # 全条件を満たすポイントは1つのはず
    center, h = center_cands[0]
    print("{} {} {}".format(center[0], center[1], h))
            

if __name__ == "__main__":
    submit()