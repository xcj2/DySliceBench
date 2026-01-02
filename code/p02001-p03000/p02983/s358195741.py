
def input_from_console():
    l, r = map(int, input().split())
    return l, r


def solve(l, r):
    minimum = 2020
    if r - l >= 2019:
        return 0
    a, b = l % 2019, r % 2019
    if r // 2019 > l // 2019:
        return 0
    for i in range(a, b):
        for j in range(a + 1, b + 1):
            minimum = min(minimum, (i * j) % 2019)
    result = minimum
    return result


def main():
    l, r = input_from_console()
    print(solve(l, r))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()
