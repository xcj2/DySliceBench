
def input_from_console():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    return n, a_list, b_list


def solve(n, a_list, b_list):
    sum_of_a = sum(a_list)
    for i in range(n):
        if a_list[i] - b_list[i] <= 0:
            b_list[i] -= a_list[i]
            a_list[i] = 0
            a_list[i + 1] -= min(b_list[i], a_list[i + 1])
        else:
            a_list[i] -= b_list[i]
    return sum_of_a - sum(a_list)


def main():
    n, a_list, b_list = input_from_console()
    print(solve(n, a_list, b_list))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()
