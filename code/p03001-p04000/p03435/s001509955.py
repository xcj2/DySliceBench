

def read_input():
    c1 = list(map(int, input().split()))
    c2 = list(map(int, input().split()))
    c3 = list(map(int, input().split()))
    return [c1, c2, c3]

# i列目を取り出す
def get_v(c, i):
    result = [c[j][i] for j in range(3)]
    return result

# i行目を取り出す
def get_h(c, i):
    result = [c[i][j] for j in range(3)]
    return result

# aとbの要素差がすべて等しいかチェック
def check_diff(a, b):
    diff = [i - j for i,j in zip(a, b)]

    d = diff[0]
    for e in diff[1:]:
        if d != e:
            return False
    return True


def submit():
    c = read_input()

    checkee = [(0, 1), (1, 2), (0, 2)]
    result = []
    for check in checkee:
        result.append(check_diff(get_v(c, check[0]), get_v(c, check[1])))
        result.append(check_diff(get_h(c, check[0]), get_h(c, check[1])))

    if all(result):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    submit()
