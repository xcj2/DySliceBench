
def read_input():
    n = int(input())
    s = input()
    ox = [c for c in s]

    return n, ox


def check_order(sw, ox):
    pre = -1
    post = 1

    for a, c in zip(sw, ox):
        if a == 'S':
            if c == 'o':
                if sw[pre] != sw[post]:
                    return False
            if c == 'x':
                if sw[pre] == sw[post]:
                    return False
        elif a == 'W':
            if c == 'o':
                if sw[pre] == sw[post]:
                    return False
            if c == 'x':
                if sw[pre] != sw[post]:
                    return False

        pre += 1
        post += 1

        if post == len(sw):
            post = 0

    return True


def get_animal(a, flip):
    if flip:
        if a == 'S':
            return 'W'
        else:
            return 'S'

    return a


def submit():
    n, ox = read_input()

    # test1
    sw = ['S', 'S']
    for i in range(1, n - 1):
        if sw[i] == 'S':
            if ox[i] == 'o':
                sw.append(get_animal(sw[i - 1], flip = False))
            else:
                sw.append(get_animal(sw[i - 1], flip = True))
        elif sw[i] == 'W':
            if ox[i] == 'o':
                sw.append(get_animal(sw[i - 1], flip = True))
            else:
                sw.append(get_animal(sw[i - 1], flip = False))

    if check_order(sw, ox):
        print(''.join(sw))
        return

    # test2
    sw = ['S', 'W']
    for i in range(1, n - 1):
        if sw[i] == 'S':
            if ox[i] == 'o':
                sw.append(get_animal(sw[i - 1], flip = False))
            else:
                sw.append(get_animal(sw[i - 1], flip = True))
        elif sw[i] == 'W':
            if ox[i] == 'o':
                sw.append(get_animal(sw[i - 1], flip = True))
            else:
                sw.append(get_animal(sw[i - 1], flip = False))

    if check_order(sw, ox):
        print(''.join(sw))
        return

    # test3
    sw = ['W', 'S']
    for i in range(1, n - 1):
        if sw[i] == 'S':
            if ox[i] == 'o':
                sw.append(get_animal(sw[i - 1], flip = False))
            else:
                sw.append(get_animal(sw[i - 1], flip = True))
        elif sw[i] == 'W':
            if ox[i] == 'o':
                sw.append(get_animal(sw[i - 1], flip = True))
            else:
                sw.append(get_animal(sw[i - 1], flip = False))

    if check_order(sw, ox):
        print(''.join(sw))
        return

    # test4
    sw = ['W', 'W']
    for i in range(1, n - 1):
        if sw[i] == 'S':
            if ox[i] == 'o':
                sw.append(get_animal(sw[i - 1], flip = False))
            else:
                sw.append(get_animal(sw[i - 1], flip = True))
        elif sw[i] == 'W':
            if ox[i] == 'o':
                sw.append(get_animal(sw[i - 1], flip = True))
            else:
                sw.append(get_animal(sw[i - 1], flip = False))

    if check_order(sw, ox):
        print(''.join(sw))
        return

    print(-1)


if __name__ == '__main__':
    submit()
