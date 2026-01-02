def parse_stdin(input_lines: int):
    data_list = []
    for i in range(input_lines):
        data_list.append(input().rstrip())
    return data_list


def find_max_interest(rates):
    min_value = rates[0]
    max_interest = -20000000000
    for i, rate in enumerate(rates[1:]):
        max_interest = max(max_interest, rate - min_value)
        min_value = min(min_value, rate)
    return max_interest


def main():
    input_lists = parse_stdin(int(input()))
    rates = list(map(int, input_lists))
    print(find_max_interest(rates))


if __name__ == '__main__':
    main()

