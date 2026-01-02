# coding=utf-8


def from_down(base, number, upper):
    return_list = []
    range_upper = min(upper+1, base+number)
    for i in range(base, range_upper):
        return_list.append(i)
    return return_list


def from_up(base, number, down):
    return_list = []
    range_down = max(base-number+1, down)
    for i in range(range_down, base+1):
        return_list.append(i)
    return return_list


def remove_double(object_list):
    list_unique = []
    for x in object_list:
        if x not in list_unique:
            list_unique.append(x)
    return list_unique


if __name__ == '__main__':
    A, B, K = map(int, input().split())
    down_list = from_down(A, K, B)
    upper_list = from_up(B, K, A)
    down_list.extend(upper_list)
    unique_list = remove_double(down_list)
    output = [print(element) for element in unique_list]
