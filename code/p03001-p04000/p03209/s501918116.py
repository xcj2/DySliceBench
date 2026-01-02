import sys

input = sys.stdin.readline
N, X = list(map(int, input().split()))


def p_num(l):
    """レベルlバーガーに含まれるパティの数を返す
    """
    return 2**(l+1)-1


def l_num(l):
    """レベルlバーガーに含まれる層の数
    """
    return 2**(l+2)-3


def p_num_l(level, x):
    """レベルlevelバーガーの1, 2, ...x層までのうちのパティーの数を返す
    """
    if level == 0:
        return 1
    if x == 1:
        return 0
    elif x == 2**(level+1)-1:
        return p_num(level-1)+1
    elif x == 2**(level**2)-3:
        return 2*p_num(level-1)+1
    elif x < 2**(level+1)-1:
        return p_num_l(level-1, x-1)
    else:
        return p_num(level-1)+1+p_num_l(level-1, x-2-l_num(level-1))


print(p_num_l(N, X))
