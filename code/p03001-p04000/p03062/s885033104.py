def solve(n, a_list):
    total = [abs(item) for item in a_list]
    negative = [abs(item) for item in a_list if item < 0]
    # print(negative)
    if len(negative) % 2 == 0:
        return sum([abs(item) for item in a_list])
    else:
        minimum = sorted(total)[0]
        return sum([abs(item) for item in a_list]) - 2 * minimum


def input_from_console():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a


def main():
    n, a_list = input_from_console()
    print(solve(n, a_list))


if __name__ == "__main__":
    main()