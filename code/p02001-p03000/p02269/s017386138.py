
PRIME = 1000231


def main():
    n = int(input())
    d = MyDict()
    for _ in range(n):
        command, v = input().split(' ')
        if command == 'insert':
            d.add(v)
        else:
            if d.find(v):
                print('yes')
            else:
                print('no')




class MyDict:

    def __init__(self, n=PRIME):
        self.n = n
        self.store = [None]*n

    def add(self, v):
        key = self._hash(v)
        while self.store[key] is not None:
            key += 1
        self.store[key] = v

    def find(self, v):
        key = self._hash(v)
        while self.store[key] is not None and self.store[key] != v:
            key += 1
        return self.store[key]

    def _hash(self, v):
        return hash(v) % self.n


if __name__ == '__main__':
    main()

