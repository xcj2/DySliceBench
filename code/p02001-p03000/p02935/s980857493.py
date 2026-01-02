def solve():
    v = read()
    result = think(v)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(v):
    local_v = list(v)
    local_v.sort()
    return recursive_call(local_v, 0, len(local_v) - 1, {})


def recursive_call(vector, from_index, to_index, cache):
    # print('{0:s}, {1:d}, {2:d}, {3:s}'.format(str(vector), from_index, to_index, str(cache)))
    key = '{0:d},{1:d}'.format(from_index, to_index)
    if key in cache:
        return cache[key]
    if to_index - from_index <= 1:
        value = (vector[from_index] + vector[to_index]) / 2
        cache[key] = value
        return value
    merged_vector = list(vector)
    elem_1 = merged_vector.pop(from_index)
    elem_2 = merged_vector.pop(from_index)
    merged_vector.insert(from_index, (elem_1 + elem_2) / 2)

    value_1 = recursive_call(merged_vector, from_index, to_index - 1, cache)
    value_2 = (elem_1 + recursive_call(vector, from_index + 1, to_index, cache)) / 2
    result = max(value_1, value_2)
    cache[key] = result

    return result


def write(result):
    print(result)


if __name__ == '__main__':
    solve()