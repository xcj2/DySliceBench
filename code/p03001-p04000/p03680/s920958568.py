def solve():
    a = read()
    result = think(a)
    write(result)


def read():
    n = read_int(1)[0]
    a = []
    for _ in range(n):
        a.append(read_int(1)[0])
    return a


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a):
    dummy = -1
    flag_for_not_visited = 0
    flag_for_visited = 1

    buttons_flash_info = list(a)
    buttons_flash_info.insert(0, dummy)

    index = 1
    visited = [flag_for_not_visited for i in range(len(buttons_flash_info))]
    visited[index] = flag_for_visited
    push_count = 1
    while True:
        next_index = buttons_flash_info[index]
        index = next_index
        if index == 2:
            return push_count
        if visited[index] == flag_for_visited:
            return -1
        visited[index] = flag_for_visited
        push_count += 1
    return -1


def write(result):
    print(result)


if __name__ == '__main__':
    solve()