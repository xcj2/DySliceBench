import sys
from collections import Counter
import random

random.seed(1)

# sys.stdin = open('b1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def gen():
    n = 301
    m = 300
    a = [[-1] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j] = 1 + (i + j) % m
    return n, m, a


def gen2(n, m):
    a = [list(range(1, m + 1)) for i in range(n)]
    for i in range(n):
        random.shuffle(a[i])
    return a


def is_possible(l, n, m, a):
    s = set(range(1, m + 1))
    choice = [0] * n
    c = Counter()
    for i in range(n):
        c[a[i][0]] += 1
    while len(s) > 0:
        update = False
        for i in range(n):
            j = choice[i]
            x = a[i][j]
            if x not in s:
                c[x] -= 1
                while a[i][j] not in s:
                    j += 1
                choice[i] = j
                x = a[i][j]
                c[x] += 1
            if c[x] > l:
                s.remove(x)
                update = True
                break
        if not update:
            return True
    return False


def solve(n, m, a):
    left, right = 1, n
    if is_possible(left, n, m, a):
        return left
    while right - left > 1:
        mid = (left + right) // 2
        if is_possible(mid, n, m, a):
            right = mid
        else:
            left = mid
    return right


def solve2(n, m, a):
    pass

    pinf = float("inf")
    best = pinf
    roop = 0
    while True:
        if roop == m:
            break

        firstlist = []
        for r in a:
            tmp = r[0]
            firstlist.append(tmp)
        mode = -1
        count = -1
        for i in range(1, m + 1):
            tmp_c = firstlist.count(i)
            if tmp_c > count:
                mode = i
                count = tmp_c
        if mode == -1:
            break
        elif count <= best:
            best = count
        for r in a:
            r.remove(mode)
        roop += 1
    return best


def check():
    n_steps = 10000
    M = 10
    n_max = 10
    m_max = 10
    for i in range(n_steps):
        n = random.randint(1, n_max)
        m = random.randint(1, m_max)

        a = gen2(n, m)
        aa = [row[:] for row in a]
        r = solve(n, m, a)
        r2 = solve2(n, m, aa)
        if r != r2:
            print('expected:', r2, 'got:', r, )
            print(n, m)
            for row in a:
                print(*row)
            print()
            # return n, m, a
            n_max -= 1
            m_max -= 1


def main():
    # check()
    solve_it()


def solve_it():
    debug = False
    if debug:
        n, m, a = gen()
    else:
        n, m = read_int_list()
        a = [read_int_list() for _ in range(n)]
    res = solve(n, m, a)
    print(res)


if __name__ == '__main__':
    main()
