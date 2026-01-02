class RKSearch:
    shift = 40
    size = 33554393

    def __init__(self, s1, s2):
        self.haystack = self._encode(s1)
        self.needle = self._encode(s2)

    def find(self):
        m, n = len(self.haystack), len(self.needle)
        if m < n:
            return

        h1 = self._hash(self.haystack, n)
        h2 = self._hash(self.needle, n)
        dm = self.shift**(n-1) % self.size

        for i in range(m-n+1):
            if h1 == h2:
                yield i
            if i+n < m:
                h1 = ((h1 - self.haystack[i]*dm) * self.shift
                      + self.haystack[i+n]) % self.size

    def _hash(self, s, length):
        h = 0
        for i in range(length):
            h = (h * self.shift + s[i]) % self.size

        return h

    def _encode(cls, s):
        basea = int.from_bytes(b'a', 'little')
        based = int.from_bytes(b'0', 'little')
        bs = []
        for c in s:
            if c.isdigit():
                bs.append(int.from_bytes(c.encode('utf8'), 'little')-based+27)
            else:
                bs.append(int.from_bytes(c.encode('utf8'), 'little')-basea)

        return bs


def run():
    s1 = input()
    s2 = input()
    rk = RKSearch(s1, s2)
    for i in rk.find():
        print(i)


if __name__ == '__main__':
    run()

