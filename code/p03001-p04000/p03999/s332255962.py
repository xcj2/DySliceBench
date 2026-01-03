
from itertools import combinations


def read_input():
    s = input().strip()
    return s

def split_and_sum(s, indice):
    indice_e = [0] + indice + [10]

    result = []
    for start,end in zip(indice_e, indice_e[1:]):
        result.append(int(s[start:end]))

    return sum(result)

def submit():
    s = read_input()
    max_index = len(s)

    acc = 0
    for i in range(max_index):
        for c in combinations(range(1, max_index), i):
            acc += split_and_sum(s, list(c))

    print(acc)

if __name__ == '__main__':
    submit()