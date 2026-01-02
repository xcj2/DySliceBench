import copy


def parse_stdin(input_lines: int):
    data_list = []
    for i in range(input_lines):
        data_list.append(input().rstrip().split())
    return data_list


def insertion_sort_with_print(values):
    print_now_state(values)
    for i, value in enumerate(values[1:]):
        i += 1
        j = i - 1
        while j >= 0 and values[j] > value:
            values[j + 1] = copy.copy(values[j])
            j -= 1
        values[j + 1] = copy.copy(value)
        print_now_state(values)


def print_now_state(values):
    for val_print in values[:-1]:
        print("{}".format(val_print), end=' ')
    print("{}".format(values[-1]), end='')
    print()


def main():
    input()
    input_lists = parse_stdin(1)
    values = list(map(int, input_lists[0]))
    insertion_sort_with_print(values)


if __name__ == '__main__':
    main()

