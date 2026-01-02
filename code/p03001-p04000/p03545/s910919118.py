A, B, C, D = map(int, list(input()))

def create_ops():
    """
    create operations.
    """
    pn = (-1, 1)
    ops = [(op_1, op_2, op_3) \
            for op_1 in pn \
            for op_2 in pn \
            for op_3 in pn]
    return ops

def sign(num):
    """
    get signed string of number.
    """
    return "+" + str(num) if num >= 0 else str(num)

def ans(a, b, c, d):
    """
    answer.
    """
    print("{0}{1}{2}{3}=7".format(a, sign(b), sign(c), sign(d)))

def main():
    """
    main.
    """
    a = A
    expected = 7 - a

    nums = (B, C, D)
    ops = create_ops()
    is_found = False

    for op in ops:
        els = [(n, pn) for n, pn in zip(nums, op)]
        els_map = map(lambda el: el[0] * el[1], els)
        els_list = list(els_map)
        total = sum(els_list)
        if total == expected:
            is_found = True
            break

    if is_found:
        b, c, d = els_list
        ans(a, b, c, d)

if __name__ == '__main__':
    main()