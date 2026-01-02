import string


def solve():
    s = read()
    result = think(s)
    write(result)


def read():
    n = read_int(1)[0]
    s = []
    for _ in range(n):
        s.append(read_line())
    return s


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(s):
    dictionary_of_histogram = {}
    for line in s:
        key_of_histgram = make_key_for_histgram(line)
        if key_of_histgram in dictionary_of_histogram:
            dictionary_of_histogram[key_of_histgram] += 1
        else:
            dictionary_of_histogram[key_of_histgram] = 1

    result = 0
    for k, v in dictionary_of_histogram.items():
        if v >= 2:
            result += combination_2(v)
    return result


def make_key_for_histgram(s):
    key = ''
    for c in string.ascii_lowercase:
        count = s.count(c)
        if count > 0:
            key += ',{0:s}{1:d}'.format(c, count)
    return key


def combination_2(n):
    return (n * (n - 1)) // 2


def write(result):
    print(result)


if __name__ == '__main__':
    solve()