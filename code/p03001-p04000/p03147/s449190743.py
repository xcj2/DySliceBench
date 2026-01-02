def main(condition, number_of_trials):
    while True:
        min_value = min(condition)
        condition = list(map(lambda x: x - min_value, condition))
        condition = remove_neighboring_zeros(condition)
        number_of_trials += min_value
        if condition == []:
            break
        if 0 not in condition:
            continue
        divided_list = divide_list_by_specified_value(condition, 0)
        for each_part_condition in divided_list:
            number_of_trials = main(each_part_condition, number_of_trials)
        break
    return number_of_trials


def divide_list_by_specified_value(list_to_be_divided, divider):
    before_idx = 0
    divided_list = []
    for idx, each_elem in enumerate(list_to_be_divided):
        if each_elem == divider:
            if list_to_be_divided[before_idx:idx] != []:
                divided_list.append(list_to_be_divided[before_idx:idx])
            before_idx = idx + 1
    if list_to_be_divided[before_idx:] != []:
        divided_list.append(list_to_be_divided[before_idx:])
    return divided_list


def remove_neighboring_zeros(array):
    while len(array) > 0 and array[-1] == 0:
        array.pop(len(array) - 1)
    while len(array) > 0 and array[0] == 0:
        array.pop(0)
    return [each_elem for idx, each_elem in enumerate(array) if
            idx == 0 or each_elem != array[idx - 1] or each_elem != 0]


if __name__ == '__main__':
    n = int(input())
    condition = list(map(int, input().split()))
    print(main(condition, 0))
