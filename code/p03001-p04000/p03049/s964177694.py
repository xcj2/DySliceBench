def input_from_console():
    n = int(input())
    s_list = []
    for i in range(n):
        s_list.append(input())
    return n, s_list


def count_ab_in_string(s_list):
    return sum([item.count('AB') for item in s_list])


def count_start_with_b(s_list):
    return sum([1 if item.startswith('B') and not item.endswith('A') else 0 for item in s_list])


def count_end_with_a(s_list):
    return sum([1 if not item.startswith('B') and item.endswith('A') else 0 for item in s_list])


def count_end_with_a_and_start_with_b(s_list):
    return sum([1 if item.endswith('A') and item.startswith('B') else 0 for item in s_list])


def main():
    n, s_list = input_from_console()
    contains_count = count_ab_in_string(s_list)
    b = count_start_with_b(s_list)
    a = count_end_with_a(s_list)
    connect_count = min(b, a)  # ..a b...


    should_be_paired = count_end_with_a_and_start_with_b(s_list)
    # print(a, b, connect_count, should_be_paired)

    if should_be_paired > 0:
        if connect_count > 0:
            print(sum([contains_count, should_be_paired, 1, connect_count - 1]))
        elif a > 0 or b > 0:
            print(sum([contains_count, should_be_paired]))
        else:
            print(sum([contains_count, should_be_paired, -1]))
    else:
        print(sum([contains_count, connect_count]))

if __name__ == "__main__":
    main()