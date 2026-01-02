class Shop:

    def __init__(self, s, p):
        self.s = str(s)
        self.p = int(p)

    def __eq__(self, other):
        return (self.s, self.p) == (other.s, other.p)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.s, -self.p) < (other.s, -other.p)

    def __le__(self, other):
        return (self.s, -self.p) < (other.s, -other.p)


def read():
    N = int(input().strip())
    shops = []
    for i in range(N):
        s, p = list(input().strip().split())
        shops.append(Shop(s, p))
    return N, shops


def solve(N, shops):
    order = sorted(range(N), key=lambda k: shops[k])
    return order


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    for i in outputs:
        print("%d" % (i + 1))