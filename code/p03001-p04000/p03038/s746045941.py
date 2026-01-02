def input_from_console():
    n, m = map(int, input().split())
    a_list = map(int, input().split())

    bc_list = []
    for i in range(m):
        b, c = map(int, input().split())
        bc_list.append((b, c))
    return n, m, a_list, bc_list


def solve(n, m, a_list, bc_list):
    bc_list.sort(key=lambda x: x[1], reverse=True)
    a_list = sorted(a_list)

    position = 0
    a_length = len(a_list)

    for item in bc_list:
        b, c = item
        for i in range(b):
            if position >= a_length or a_list[position] >= c:
                return sum(a_list)
            else:
                a_list[position] = c
                position += 1
    return sum(a_list)


def main():
    n, m, a_list, bc_list = input_from_console()
    print(solve(n, m, a_list, bc_list))


if __name__ == "__main__":
    main()