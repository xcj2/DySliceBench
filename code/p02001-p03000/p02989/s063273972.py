
def input_from_console():
    n = int(input().strip())
    d_list = list(map(int, input().strip().split()))
    return n, d_list


def solve(n, d_list):
    result = 0
    divider = n //2
    d_list.sort()
    pre = d_list[:divider]
    lower = max(pre) + 1
    post = d_list[divider:]
    upper = min(post)
    if lower <= upper:
        result = upper - lower + 1
    return result


def main():
    n, d_list = input_from_console()
    print(solve(n, d_list))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()
