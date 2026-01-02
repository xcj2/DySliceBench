"""
A - Limited Insertion
"""


def solve():
    N = int(input())
    b = list(map(int, input().split()))
    ans = make_list(b, 0, [])

    if ans == -1:
        print(ans)
    else:
        for a in list(reversed(ans)):
            print(a)
        # ans = list(reversed(ans))
        # ans = [str(i) for i in ans]
        # print(' '.join(ans))


def make_list(b: list, x: int, ans: list):
    re = -1
    # print('try {}'.format(x))
    # print(b)

    if len(b) == 0:
        return ans

    if check_list(b) is False:
        return re

    for i, element in enumerate(b, 1):
        if i == element:
            b_c = b.copy()
            ans_c = ans.copy()
            ans_c.append(b_c[i - 1])
            b_c.remove(element)  # 除去対象は自分より前に同じ要素が存在しない
            # print('match element {}'.format(element))
            # print(ans)
            tmp = make_list(b_c, x + 1, ans_c)
            if tmp != -1:
                re = tmp
                break
    # print('return {} is '.format(x), re)
    return re


def check_list(b):
    re = True
    for i, element in enumerate(b, 1):
        if i < element:
            re = False
            break
    return re


if __name__ == '__main__':
    solve()
