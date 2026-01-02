def is_horizontal_same(s):
    for j in range(0, len(s)):
        if s[j] != ".":
            return False
    return True


def is_vertical_same(str_list, i):
    for j in range(0, len(str_list)):
        if str_list[j][i] != ".":
            return False
    return True


def main():
    h, w = map(int, input().split())

    str_list = []
    for i in range(0, h):
        str_list.append(input())

    while True:
        is_completed = True

        same_line_indexes = []
        for i in range(0, len(str_list)):
            if is_horizontal_same(str_list[i]):
                same_line_indexes.append(i)
                is_completed = False
        popped_cnt = 0
        for i, v in enumerate(same_line_indexes):
            str_list.pop(v - popped_cnt)
            popped_cnt += 1

        same_vertical_line_indexes = []
        for i in range(0, len(str_list[0])):
            if is_vertical_same(str_list, i):
                same_vertical_line_indexes.append(i)
                is_completed = False
        popped_cnt = 0
        for i, v in enumerate(same_vertical_line_indexes):
            for j in range(0, len(str_list)):
                org_str = str_list[j]
                str_list[j] = org_str[:v - popped_cnt] + org_str[v - popped_cnt + 1:]
            popped_cnt += 1

        if is_completed:
            break

    for i, v in enumerate(str_list):
        print(v)


main()
