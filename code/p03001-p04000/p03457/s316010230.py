import unittest


def is_ある時刻での判定(t, d):
    # 時刻t >= d でないと実現不可能
    if t < d:
        return True

    # 偶奇が一致しないと実現不可能
    if not (t % 2 == d % 2):
        return True

    return False


def can_not_realize(N, t_list, x_list, y_list) -> bool:
    # 各時刻ごとの判定
    for t, x, y in zip(t_list, x_list, y_list):
        d = x + y

        if is_ある時刻での判定(t, d):
            return True

    # t_n と t_n+1 間 での移動判定
    for i in range(N):
        if i + 1 >= N:
            break

        t = t_list[i + 1] - t_list[i]
        diff_x = abs(x_list[i + 1] - x_list[i])
        diff_y = abs(y_list[i + 1] - y_list[i])

        d = diff_x + diff_y

        if is_ある時刻での判定(t, d):
            return True

    return False


def actual(N, t_list, x_list, y_list):
    if can_not_realize(N, t_list, x_list, y_list):
        return 'No'

    return 'Yes'

N = int(input())

t_list, x_list, y_list = [], [], []
for _ in range(N):
  t, x, y = list(map(int, input().split()))
  t_list.append(t)
  x_list.append(x)
  y_list.append(y)
  
print(actual(N, t_list, x_list, y_list))
  