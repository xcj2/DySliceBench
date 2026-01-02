import sys

def solve():
    n, list_of_xy = read()
    result = think(n, list_of_xy)
    write(result)


def read():
    n, m = read_int(2)
    list_of_xy = []
    for i in range(m):
        list_of_xy.append(read_int(2))
    return n, list_of_xy


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(n, list_of_xy):
    num_of_input_edges = [0 for _ in range(n + 1)]
    num_of_output_edges = [0 for _ in range(n + 1)]

    linked_list = generate_linked_list(list_of_xy)

    invalid_value = -1
    length_of_longest_path_start_from = [invalid_value for _ in range(n + 1)]

    for x, y in list_of_xy:
        num_of_input_edges[y] += 1
        num_of_output_edges[x] += 1

    for i in range(1, len(num_of_input_edges)):
        if num_of_output_edges[i] == 0:
            length_of_longest_path_start_from[i] = 0

    for i in range(1, len(num_of_input_edges)):
        if num_of_input_edges[i] == 0:
            update_logest_path_start_from(i, linked_list, length_of_longest_path_start_from, invalid_value)

    return max(length_of_longest_path_start_from)


def generate_linked_list(list_of_xy):
    linked_list = {}
    for x, y in list_of_xy:
        if x in linked_list:
            linked_list[x].append(y)
        else:
            linked_list[x] = [y]
    return linked_list


def update_logest_path_start_from(x, linked_list, length_of_longest_path_start_from, invalid_value):
    if length_of_longest_path_start_from[x] != invalid_value:
        return

    dest_from_x = linked_list.get(x, [])
    for y in dest_from_x:
        if length_of_longest_path_start_from[y] == invalid_value:
            update_logest_path_start_from(y, linked_list, length_of_longest_path_start_from, invalid_value)
            length_of_longest_path_start_from[x] = max(length_of_longest_path_start_from[x], length_of_longest_path_start_from[y] + 1)
        else:
            length_of_longest_path_start_from[x] = max(length_of_longest_path_start_from[x], length_of_longest_path_start_from[y] + 1)


def write(result):
    print(result)


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 5)
    solve()