
from math import sqrt
class Vector:
    def __init__(self, ls):
        """ls = list"""
        self.vec = ls

    def __len__(self):
        return len(self.vec)

    def __getitem__(self, idx):
        return self.vec[idx]

    def __repr__(self):
        return f'Vector({self.vec})'

    def add(self, vec):
        """vec: Vector class"""
        assert len(self) == len(vec)
        ret = [a + b for a, b in zip(self.vec, vec.vec)]
        return Vector(ret)

    def sub(self, vec):
        """vec: Vector class"""
        assert len(self) == len(vec)
        ret = [a - b for a, b in zip(self.vec, vec.vec)]
        return Vector(ret)

    def mul(self, vec):
        """vec: Vector class"""
        assert len(self) == len(vec)
        ret = [a * b for a, b in zip(self.vec, vec.vec)]
        return Vector(ret)

    def norm(self):
        tmp = sum([x * x for x in self.vec])
        return sqrt(tmp)


def norm(vec):
    """
    vec ... Vector class
    """
    return vec.norm()


def cross(a, b):
    """
    Outer product for 2d
    a,b ... Vector class
    """
    assert len(a) == 2 and len(b) == 2
    first = a[0] * b[1]
    second = a[1] * b[0]
    return first - second


def dot(a, b):
    return sum(a.mul(b))

def resolve():
    Q = int(input())

    for i in range(Q):
        s, t, a, b, x, y, c, d = map(int, input().split())
        P0 = Vector([s, t])
        P1 = Vector([a, b])
        P2 = Vector([x, y])
        P3 = Vector([c, d])

        line_a = P1.sub(P0)
        line_b = P3.sub(P2)

        if cross(line_a, line_b) == 0:
            print(2)
        elif dot(line_a, line_b) == 0:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    resolve()

