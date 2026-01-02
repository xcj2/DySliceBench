# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_D
# O(n**2)のプログラムを書かないように注意

import sys
read = sys.stdin.readline


def read_ints():
    return list(map(int, read().split()))


def read_a_int():
    return int(read())


def read_matrix(H):
    '''
    H is number of rows
    '''
    return [list(map(int, read().split())) for _ in range(H)]


def read_map(H):
    '''
    H is number of rows
    文字列で与えられた盤面を読み取る用
    '''
    return [read()[:-1] for _ in range(H)]


def read_col(H, n_cols):
    '''
    H is number of rows
    n_cols is number of cols

    A列、B列が与えられるようなとき
    '''
    ret = [[] for _ in range(n_cols)]
    for _ in range(H):
        tmp = list(map(int, read().split()))
        for col in range(n_cols):
            ret[col].append(tmp[col])

    return ret


n = read_a_int()
R = read_col(n, 1)[0]

# dp的な考え方？
# 各時刻における損益の最大値は、前の時刻における損益の最大値と現時刻の最小値から計算可能
# 最小値にぶち当たるたびに、そこにひっつきながら収益がもっと上がるか見張る感じ

r_min = R[0]
ans = -10**9
for r in R[1:]:
    ans = max(ans, r-r_min)
    r_min = min(r, r_min)

print(ans)

