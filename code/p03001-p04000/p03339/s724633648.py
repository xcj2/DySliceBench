def solve():
    s = read()
    result = think(s)
    write(result)


def read():
    n = read_int(1)[0]
    return read_line(n=n)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(s):
    accumulated_count_facing_east, accumulated_count_facing_west = preprocess(s)
    member_count_needed_to_change_direction = len(s)  # as initial value

    n = len(s)

    for i in range(len(s)):
        if i == 0:
            change_to_west = accumulated_count_facing_east[n - 1] - accumulated_count_facing_east[0]
            member_count_needed_to_change_direction = min(change_to_west, member_count_needed_to_change_direction)
        elif i == len(s) - 1:
            change_to_east = accumulated_count_facing_west[n - 2]
            member_count_needed_to_change_direction = min(change_to_east, member_count_needed_to_change_direction)
        else:
            change_to_east = accumulated_count_facing_west[i - 1]
            change_to_west = accumulated_count_facing_east[n - 1] - accumulated_count_facing_east[i]
            member_count_needed_to_change_direction = min(change_to_east + change_to_west, member_count_needed_to_change_direction)
    return member_count_needed_to_change_direction


def preprocess(s):
    east_symbol = 'E'
    west_symbol = 'W'
    accumulated_count_facing_east = [0 for x in range(len(s))]
    accumulated_count_facing_west = [0 for x in range(len(s))]
    for i, elem in enumerate(s):
        if i == 0:
            if elem == east_symbol:
                accumulated_count_facing_east[i] = 1
            else:
                accumulated_count_facing_west[i] = 1
        else:
            if elem == east_symbol:
                accumulated_count_facing_east[i] = accumulated_count_facing_east[i - 1] + 1
                accumulated_count_facing_west[i] = accumulated_count_facing_west[i - 1]
            else:
                accumulated_count_facing_east[i] = accumulated_count_facing_east[i - 1]
                accumulated_count_facing_west[i] = accumulated_count_facing_west[i - 1] + 1
    return accumulated_count_facing_east, accumulated_count_facing_west

def write(result):
    print(result)


if __name__ == '__main__':
    solve()