
def input_from_console():
    n = int(input().rstrip())

    s_list = []
    for i in range(1, n+1):
        s, p = input().split()
        p = int(p)
        s_list.append((i, s, p))
    return n, s_list


def solve(n, s_list):

    final_order = []
    city_list = set([item[1] for item in s_list])
    city_list_sorted = sorted(city_list)
    for city in city_list_sorted:
        ranked_list = [item for item in s_list if item[1] == city]
        final_order.extend([item[0] for item in sorted(ranked_list, key=lambda x: x[2], reverse=True)])
    return '\n'.join(map(str, final_order))


def main():
    n, s_list = input_from_console()
    print(solve(n, s_list))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()
