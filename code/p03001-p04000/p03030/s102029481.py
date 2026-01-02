def input_from_console():
    n = int(input().rstrip())

    s_list = []
    for i in range(1, n + 1):
        s, p = input().split()
        p = int(p)
        s_list.append((i, s, p))
    return n, s_list


def solve(n, s_list):
    sorted_city_list = sorted(s_list, key=lambda x: (x[1], -x[2]))
    return '\n'.join(map(str, [item[0] for item in sorted_city_list]))


def main():
    n, s_list = input_from_console()
    print(solve(n, s_list))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()
