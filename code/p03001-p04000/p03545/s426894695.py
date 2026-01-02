def solve():
    s_abcd = read()
    result = think(s_abcd)
    write(result)


def read():
    return read_line(n=4)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(s_abcd):
    list_int_abcd = list(map(lambda x: int(x), list(s_abcd)))
    max_patterns = 2 ** 3
    expected_answer = 7

    for _ in range(max_patterns):
        formula_string = generate_formula_string_with(list_int_abcd, _)
        if eval(formula_string) == expected_answer:
            return format_formula_string(formula_string, expected_answer)
    raise RuntimeError()


def generate_formula_string_with(list_int_abcd, bit):
    shift = 3
    operator = ['+', '-']
    formula_string = ''
    for i, elem in enumerate(list_int_abcd):
        formula_string += str(elem)
        if i == len(list_int_abcd) - 1:
            continue
        if bit >> (shift - i - 1) & 1:
            formula_string += operator[0]
        else:
            formula_string += operator[1]
    return formula_string


def format_formula_string(formula_string, expected_answer):
    return '{0:s}={1:s}'.format(formula_string, str(expected_answer))


def write(result):
    print(result)


if __name__ == '__main__':
    solve()