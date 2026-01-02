def input_from_console():
    n = int(input())
    w_list = list(map(int, input().split()))
    return n, w_list


def solve(n, w_list):
    min_weight = max(w_list)
    for i in range(len(w_list)):
        min_weight = min(abs(sum(w_list[0:i])-sum(w_list[i:])), min_weight)
    return min_weight


def main():
    n, w_list = input_from_console()
    print(solve(n, w_list))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()
