

from itertools import product


def read_input():
    n = int(input())
    testimonies = {}

    for i in range(n):
        testimonies[i] = []
        a = int(input())
        for _ in range(a):
            x, y = map(int, input().split())
            testimonies[i].append((x - 1, y))

    return n, testimonies


def contradict(pattern, testimonies):
    for i, p in enumerate(pattern):
        if not p:
            continue
        else:
            for x, y in testimonies[i]:
                if pattern[x] != int(y):
                    return True    
    return False
            


def submit():
    n, testimonies = read_input()

    for pattern in product([True, False], repeat=n):
        if not contradict(pattern, testimonies):
            print(sum(pattern))
            break


if __name__ == "__main__":
    submit()