def get_two_int():
    two_int = input().split()
    for i in range(2):
        two_int[i] = int(two_int[i])
    return two_int

def make_sorted_num_list(num):
    num_list = [None] * num
    for i in range(num):
        num_list[i] = int(input())
    sorted_num_list = sorted(num_list)
    return sorted_num_list

def shuffle(first_list, second_list):
    flag = False
    dif_value = sum(first_list) - sum(second_list)
    if abs(dif_value) % 2 != 0:
        return flag, -1
    for i in first_list:
        for j in second_list:
            if i - j == (dif_value // 2):
                flag = True
                return flag, i, j
    return flag, -1


if __name__ == "__main__":
    while True:
        taro_num, hanako_num = get_two_int()
        if taro_num == hanako_num == 0:
            break
        taro_list = make_sorted_num_list(taro_num)
        hanako_list = make_sorted_num_list(hanako_num)
        ans = shuffle(taro_list, hanako_list)
        if ans[0] == False:
            print(ans[1])
        else:
            print(ans[1], ans[2])

