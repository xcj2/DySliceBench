def solve():
    a, b, c = read()
    result = think(a, b, c)
    write(result)


def read():
    return read_int(3)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a, b, c):
    m_seed = a % b
    while m_seed >= b:
        m_seed %= b

    visited = set()
    m_accumulated = m_seed
    while True:
        if m_accumulated == c:
            return True
        if m_accumulated in visited:
            return False
        visited.add(m_accumulated)
        m_accumulated += m_seed
        while m_accumulated >= b:
            m_accumulated %= b


def write(result):
    if result:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    solve()