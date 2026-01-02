
def input_from_console():
    n = int(input())
    p_list = list(map(int, input().split()))
    return n, p_list


def solve(n, p_list):
    p_list_sorted = sorted(p_list)
    diff_count = 0
    for i in range(len(p_list)):
        if p_list_sorted[i] != p_list[i]:
            diff_count += 1

    if diff_count > 2:
        return 'NO'
    return 'YES'


def main():
    n, p_list = input_from_console()
    print(solve(n, p_list))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()
