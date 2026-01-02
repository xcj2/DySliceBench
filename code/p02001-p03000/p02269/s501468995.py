# ALDS1_4_C
import sys
M = 1046527


def h1(key):
    return key % M


def h2(key):
    return 1 + (key % (M - 1))


def h(key, i):
    return(h1(key) + i * h2(key)) % M


def getChar(gene):
    if gene == 'A':
        return 1
    elif gene == 'C':
        return 2
    elif gene == 'G':
        return 3
    else:
        return 4


def getkey(gene):
    sum = 0
    p = 1
    for i in gene:
        sum += p * getChar(i)
        p *= 5
    return sum


class HashDict:
    def __init__(self):
        self.key = [None] * (2 * 10 ** 6)

    def insert(self, key):
        i = 0
        while True:
            j = h(key, i)
            if self.key[j] is None:
                self.key[j] = key
                return
            else:
                i += 1

    def find(self, key):
        i = 0
        while True:
            j = h(key, i)
            # print('find j : {}'.format(j))
            if self.key[j] == key:
                return True
            elif self.key[j] is None or i > M:
                return None
            else:
                i += 1


n = int(input())
T = HashDict()

for i in range(n):
    command, key = sys.stdin.readline().strip().split()
    key = getkey(key)
    # print('i : {}  key : {}'.format(i, key))
    if command == 'insert':
        T.insert(key)
    elif command == 'find':
        if T.find(key):
            print('yes')
        else:
            print('no')



