class Dict(object):
    def __init__(self, size):
        self.dict = [None for _ in range(size)]
        self.size = size

    def h1(self, key):
        return key % self.size

    def h2(self, key):
        return 1 + (key % (self.size-1))

    def h(self, key, i):
        return (self.h1(key) + i * self.h2(key)) % self.size

    def insert(self, key):
        i = 0
        while True:
            j = self.h(key, i)
            if self.dict[j] == None:
                self.dict[j] = key
                break
            else:
                i += 1

    def find(self, key):
        i = 0
        while True:
            j = self.h(key, i)
            if self.dict[j] == key:
                return 1
            elif self.dict[j] == None or i >= self.size:
                return 0
            else:
                i += 1


def get_key(table, word):
    return int(word.translate(table))


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline # faster input

    table = str.maketrans({
        "A": "1",
        "C": "2",
        "G": "3",
        "T": "4"
    })

    m = 1046527
    d = Dict(m)

    n = int(input())

    for _ in range(n):
        command = input()
        if command[0] == 'i':
            d.insert(get_key(table, command[7:]))
        else:
            if d.find(get_key(table, command[5:])):
                print('yes')
            else:
                print('no')

