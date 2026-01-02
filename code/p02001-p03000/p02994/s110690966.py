
def input_from_console():
    n, l = map(int, input().split())
    return n, l


def solve(n, l):
    all_data = [ l + item for item in range(n)]
    new_list = sorted([abs(item) for item in all_data])
    if new_list[0] in all_data:
        result = sum(all_data) - new_list[0]
    else:
        result = sum(all_data) + new_list[0]
    return result


def main():
    n, l = input_from_console()
    print(solve(n, l))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()