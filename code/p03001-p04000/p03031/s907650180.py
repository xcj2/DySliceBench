def input_from_console():
    n, m = map(int, input().split())
    k_list = []

    for i in range(m):
        k, *s_list = map(int, input().split())
        k_list.append((k, s_list))
    p_list = list(map(int, input().split()))
    return n, m, k_list, p_list


def solve(n, m, k_list, p_list):
    def bit_count(bit):
        count = 0
        while bit > 0:
            if bit & 1:
                count += 1
            bit >>= 1
        return count

    selected_light_list = []
    for i in range(m):
        bit_sum = 0
        target = k_list[i][1]
        for j in target:
            bit_sum += 2 ** int(j - 1)
        selected_light_list.append(bit_sum)

    total_count = 0
    for sp in range(2 ** n):
        # print('sp {0:b}'.format(sp))
        condition_list = []
        for i in range(m):
            if  bit_count(selected_light_list[i] & sp) % 2 == p_list[i]:
                condition_list.append(True)
            else:
                condition_list.append(False)
        if all(condition_list):
            total_count += 1
    return total_count


def main():
    n, m, k_list, p_list = input_from_console()
    print(solve(n, m, k_list, p_list))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()
