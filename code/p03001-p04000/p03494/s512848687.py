def check_mod(target_list):
    for target in target_list:
        if int(target) % 2 != 0:
            return False
    else:
        return True


def replace_target(target_list):
    new_list = list()
    for target in target_list:
        new_list.append(int(target) / 2)
    return new_list


def main():
    target_num = input()
    target_list = input().split()

    repeat_count = 0

    while True:
        repeat_flg = check_mod(target_list)
        if repeat_flg:
            target_list = replace_target(target_list)
            repeat_count += 1
        else:
            print(repeat_count)
            break


if __name__ == '__main__':
    main()
