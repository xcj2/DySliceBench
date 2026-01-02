from collections import defaultdict

def mapt(fn, *args):
    return tuple(map(fn, *args))


def Atom(strings):
    return int(strings) if strings.isdigit() else strings


def symmetric(setseq):
    a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
    return a^setseq

    
n = int(input())
dataset = [mapt(Atom, input().split(" ")) for i in range(n)]
a = defaultdict(list)

for key, value in dataset:
    a[key].append(value)

for key, value in a.items():
    a[key] = symmetric(set(value))
    
for i in ("S", "H", "C", "D"):
    for value in (a.get(i)):
        print(i, value)
