def bubleSort(table):
    table = table.copy()
    for nAchieve in range(len(table)):
        for i in range(len(table) - 1, nAchieve, -1):
            if table[i][1] < table[i - 1][1]:
                table[i], table[i - 1] = table[i - 1], table[i]
    return table


def selectionSort(table):
    table = table.copy()
    for nAchieve in range(len(table)):
        minimum_index = nAchieve
        for i in range(nAchieve + 1, len(table)):
            if table[minimum_index][1] > table[i][1]:
                minimum_index = i
        if minimum_index != nAchieve:
            table[nAchieve], table[minimum_index] = table[minimum_index], table[nAchieve]
    return table


def checkStable(stable, comparison):
    if stable == comparison:
        return 'Stable'
    else:
        return 'Not stable'


element = int(input())
table = list(map(str, input().split()))

y = selectionSort(table)
x = bubleSort(table)
print(' '.join(map(str, x)))
print('Stable')
print(' '.join(map(str, y)))
print(checkStable(x, y))

