def data_assignment():
    for i in range(r):
        for j, e in enumerate(map(int, input().split())):
            table[i][j] = e

def total_rows():
    for i, line in enumerate(table):
        table[i][c] = sum(line[:c])


def total_columns():
    for i, line in enumerate(table):
        if i == r:
            break
        for j, element in enumerate(line):
            table[r][j] += element


def table_print():
    for line in table:
        for i, element in enumerate(line):
            if i == c:
                print(element)
            else:
                print(element, end=' ')


r, c = map(int, input().split())
table = [[0 for i in range(c+1)] for j in range(r+1)]
data_assignment()
total_rows()
total_columns()
table_print()

