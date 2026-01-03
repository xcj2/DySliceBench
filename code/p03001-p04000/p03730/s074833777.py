
def read_input():
    a, b, c = map(int, input().split())
    return a, b, c


def mymod(x, y):
    return x % y

def submit():
    a, b, c = read_input()

    mods = list(set([mymod(i*a, b) for i in range(1, b)]))
    mods.sort()

    while True:
        temp = []
        for i in range(len(mods)):
            for j in range(len(mods)):
                temp.append(mymod(mods[i] + mods[j], b))
        new_mods = list(set(mods + temp))
        new_mods.sort()

        if mods == new_mods:
            break

        mods = new_mods

    if c in mods:
        print('YES')
    else:
        print('NO')



if __name__ == '__main__':
    submit()