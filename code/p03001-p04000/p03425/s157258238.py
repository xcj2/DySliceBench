

def read_input():
    n = int(input())

    names = []
    for i in range(n):
        names.append(input())

    return n, names


# MARCHのうち3つの取り出すパターンを作成
def initial_pattern():
    return [
        ['A', 'M', 'R'],
        ['A', 'C', 'M'],
        ['A', 'H', 'M'],
        ['C', 'M', 'R'],
        ['H', 'M', 'R'],
        ['C', 'H', 'M'],
        ['A', 'C', 'R'],
        ['A', 'H', 'R'],
        ['A', 'C', 'H'],
        ['C', 'H', 'R']]


def submit():
    n, names = read_input()

    name_file = {'M':[], 'A':[], 'R':[], 'C':[], 'H':[]}
    for n in names:
        if n[0] in 'MARCH':
            name_file[n[0]].append(n)

    count = 0
    initials = initial_pattern()

    for initial in initials:
        count += len(name_file[initial[0]]) * len(name_file[initial[1]]) * len(name_file[initial[2]])

    print(count)

if __name__ == '__main__':
    submit()
