import numpy as np
N = int(input())
h = list(map(int, input().split()))
diff = np.array([i for i in h])


# 右から見ていったときに、最小値までの数値と、それ以降昇順になっている値までに最小値を足す
# 以降それを繰り返す
def find_min_idx(l):
    # 0以外で最小の値を取得
    non_0_list = [i for i in l if i != 0]
    min_value = min(non_0_list)
    min_idx = np.where(l == min_value)[0][0]
    return min_idx


def get_min_value(l, min_idx):
    return l[min_idx]


def get_end_idx(l, min_idx, min_value):
    for idx, i in enumerate(l):
        if idx > min_idx:
            if i == 0:
                return idx - 1
            if i < min_value or i == 0:
                return idx - 1
    else:
        return len(l) - 1


def find_start_idx(l, min_idx):
    if len(l[:min_idx]) == 0:
        return 0
    for idx, i in enumerate(reversed(l[:min_idx])):
        if i == 0:
            return idx
    else:
        return len(l[:min_idx])-1


count = 0
while not all([i == 0 for i in diff]):
    #  print(count, diff)
    #  import pdb
    #  pdb.set_trace()
    min_idx = find_min_idx(diff)
    min_value = get_min_value(diff, min_idx)
    end_idx = get_end_idx(diff, min_idx, min_value)
    start_idx = find_start_idx(diff, min_idx)
    #  print('min_idx, end_idx, start_idx', min_idx, end_idx, start_idx)
    #  import pdb
    #  pdb.set_trace()
    for idx, i in enumerate(diff):
        if i == 0:
            continue

        if idx <= end_idx:
            if idx >= min_idx - start_idx - 1:
                diff[idx] -= min_value
            elif idx >= min_idx:
                diff[idx] -= min_value

    count += min_value

    #  print(count, diff, '\n')

print(count)
