A = [[1, 1], [1, 1]]
B = [[1], [1], [1], [1]]
C = [[1, 1, 1, 1]]
D = [[0, 1], [1, 1], [1, 0]]
E = [[1, 1, 0], [0, 1, 1]]
F = [[1, 0], [1, 1], [0, 1]]
G = [[0, 1, 1], [1, 1, 0]]


def f(_h, _w, flg):
    for h in range(8-_h+1):
        for w in range(8-_w+1):
            big = f1(h, w, _h, _w)
            if f2(big, flg):
                return True


def f1(s_h, s_w, _h, _w):
    big = []
    for h in range(_h):
        w_line = []
        for w in range(_w):
            w_line.append(maps[s_h+h][s_w+w])
        big.append(w_line)
    return big


def f2(big, flg):
    if flg == 'A':
        return bool(big == A)
    elif flg == 'B':
        return bool(big == B)
    elif flg == 'C':
        return bool(big == C)
    elif flg == 'D':
        return bool(big == D)
    elif flg == 'E':
        return bool(big == E)
    elif flg == 'F':
        return bool(big == F)
    elif flg == 'G':
        return bool(big == G)


def display():
    if f(2, 2, 'A'):
        print('A')
    elif f(4, 1, 'B'):
        print('B')
    elif f(1, 4, 'C'):
        print('C')
    elif f(3, 2, 'D'):
        print('D')
    elif f(2, 3, 'E'):
        print('E')
    elif f(3, 2, 'F'):
        print('F')
    elif f(2, 3, 'G'):
        print('G')

while True:
    try:
        maps = []
        for _ in range(8):
            maps.append(list(map(int, input())))
        display()
        input()
    except EOFError:
        break