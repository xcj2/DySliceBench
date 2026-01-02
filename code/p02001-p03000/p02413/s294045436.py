r = 0
c = 0


def input_size():
    global r, c
    r, c = map(int, input().split(' '))


def input_table(table):
    for i in range(0, r):
        vs = list(map(int, input().split(' ')))
        row = []
        for v in vs:
            row.append(v)
        table.append(row)


def calc_total(table):
    total = []
    for i in range(0, c + 1):
        total.append(0)

    for i in range(0, r + 1):
        if i < r:
            t = 0
            for j in range(0, c):
                t += table[i][j]
                total[j] += table[i][j]
            table[i].append(t)
            total[c] += t

        if i == r - 1:
            table.append(total)


def output(vs):
    for row in vs:
        first = True
        for v in row:
            if not first:
                print(end=' ')
            print(v, end='')
            first = False
        print()


input_size()
vs = []
input_table(vs)
calc_total(vs)
output(vs)

