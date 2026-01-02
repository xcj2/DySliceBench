# 入力が10**5とかになったときに100ms程度早い
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


N = read_a_int()
D = read_ints()

if D[0] != 0:
    print(0)
    exit()


# 飛んだらアウト
# 個数を数えてどうにかする
# D.sort()
# if D[1] == 0:
#     print(0)
#     exit()

# now = 0
# cnt = 0
# ans = 1
# pre_cnt = 0
# for d in D:
#     if d == now + 1:
#         ans *= cnt
#         pre_cnt = now
#         now = d
#         cnt = 0
#     elif d == now:
#         cnt += 1


from collections import Counter
dic = Counter(D)
ans = 1

if dic[0] != 1:
    print(0)
    exit()
# print(dic)
for i in range(max(D)):
    # もし連続してなかったらだめ
    try:
        dic[i + 1]
    except:
        print(0)
        exit()

    ans *= dic[i]**dic[i + 1]
    if ans > 998244353:
        ans = ans % 998244353

print(ans)
