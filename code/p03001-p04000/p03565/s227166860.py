sp = input()
t = input()


def is_valid(start):
    for i in range(len(t)):
        c = sp[start+i]
        if c != '?' and c != t[i]:
            return False
    return True


def minstr(start):
    end = start + len(t)
    sa = []
    for i, c in enumerate(sp):
        if i >= start and i < end:
            sa.append(t[i - start])
            continue
        if c == '?':
            sa.append('a')
        else:
            sa.append(c)
    return ''.join(sa)


def solve():
    if len(t) > len(sp):
        return False
    start = len(sp) - len(t)
    while start >= 0:
        if is_valid(start):
            print(minstr(start))
            return True
        start -= 1
    return False


if not solve():
    print('UNRESTORABLE')
