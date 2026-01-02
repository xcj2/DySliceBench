
def read_input():
    s = input()
    a, b, c, d = map(int, [c for c in s])

    return a, b, c, d


def check_formulae(a, b, c, d):
    if a + b + c + d == 7:
        print('{}+{}+{}+{}=7'.format(a,b,c,d))
        return
    if a + b + c - d == 7:
        print('{}+{}+{}-{}=7'.format(a,b,c,d))
        return
    if a + b - c + d == 7:
        print('{}+{}-{}+{}=7'.format(a,b,c,d))
        return
    if a + b - c - d == 7:
        print('{}+{}-{}-{}=7'.format(a,b,c,d))
        return
    if a - b + c + d == 7:
        print('{}-{}+{}+{}=7'.format(a,b,c,d))
        return
    if a - b + c - d == 7:
        print('{}-{}+{}-{}=7'.format(a,b,c,d))
        return
    if a - b - c + d == 7:
        print('{}-{}-{}+{}=7'.format(a,b,c,d))
        return
    if a - b - c - d == 7:
        print('{}-{}-{}-{}=7'.format(a,b,c,d))
        return
    return


def submit():
    a, b, c, d = read_input()
    check_formulae(a, b, c, d)

if __name__ == '__main__':
    submit()