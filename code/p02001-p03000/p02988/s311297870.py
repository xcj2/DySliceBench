def input_from_console():
    n = int(input())
    p_list= list(map(int, input().strip().split()))
    return n, p_list


def solve(n, p_list):
    result = 0
    if n <= 2:
        return result
    for i in range(n - 2):
        if min(p_list[i], p_list[i+2]) < p_list[i+1] and max(p_list[i], p_list[i+2]) > p_list[i+1]:
            result += 1
    return result


def main():
    n, p_list = input_from_console()
    print(solve(n, p_list))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()