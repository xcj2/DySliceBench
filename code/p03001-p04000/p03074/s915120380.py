def mark_zero1(s):
    index = [i for i, s_ in enumerate(s) if s_ == "0" and safe_get(s, i - 1) != "0"]
    return index


def mark_zero2(s):
    index = [i for i, s_ in enumerate(s) if s_ == "0" and safe_get(s, i + 1) != "0"]
    return index


def safe_get(lis, index):
    if index < 0:
        return -1
    elif index >= len(lis):
        return len(s)
    else:
        return lis[index]


def get_score(a, b, i, j):
    return safe_get(a, j + 1) - safe_get(b, i - 1) - 1


n, k = list(map(int, input().split(" ")))
s = input()
a = mark_zero1(s)
b = mark_zero2(s)


try_num = min(len(a), k)
ij_list = [(idx, idx + try_num - 1) for idx in range(len(a) - try_num + 1)]

print(max([get_score(a, b, i, j) for i, j in ij_list]))
