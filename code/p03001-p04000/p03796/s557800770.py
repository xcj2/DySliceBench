def solve():
    n = read()
    result = think(n)
    write(result)


def read():
    return read_int(1)[0]


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(n):
    p = 10 ** 9 + 7
    return mod_fact(n, p)

def mod_fact(n, p):
    if n == 1:
        return 1 % p

    result = 1 % p
    for i in range(n):
        r_1 = result % p
        r_2 = (i + 1) % p
        result = (r_1 * r_2) % p
    return result

def write(result):
   print(result)


if __name__ == '__main__':
    solve()