def find_lakes(diagram):
    """Find lakes in diagram.

    >>> pat = str.maketrans('ufd', '/_\\\\')
    >>> find_lakes('ddfuu'.translate(pat))
    [6]
    >>> find_lakes('dduuudfududdddufudduuuffdddfddufdufud'.translate(pat))
    [4, 2, 1, 19, 9]
    >>> find_lakes('ff'.translate(pat))
    []
    """
    def calc_areas(ls):
        areas = []
        e1, e2 = 0, 0
        for n, m in reversed(ls):
            if e1 < n and e2 > m:
                area = areas.pop()
                areas.append(area + (m - n))
            else:
                areas.append(m - n)
                e1, e2 = n, m
        return areas[::-1]

    lakes = []
    slopes = []

    for i, c in enumerate(diagram):
        if c == '\\':
            slopes.append(i)
        elif c == '/':
            if len(slopes) > 0:
                lakes.append((slopes.pop(), i))

    return calc_areas(lakes)


def run():
    ls = find_lakes(input())

    summary = [str(len(ls))] + [str(i) for i in ls]
    print(sum(ls))
    print(" ".join(summary))


if __name__ == '__main__':
    run()

