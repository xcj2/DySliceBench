# encoding: "utf-8"

from enum import Enum

class Unreachable(Exception):
    pass

class Type(Enum):
    VAL = 0
    PTR = 1


class Elem:
    def __init__(self, i, value, _type):
        self.idx = i
        self.value = value
        self.type = _type

    def set(self, value, _type):
        self.value = value
        self.type = _type
        

class SetManager:
    def __init__(self, n):
        self.data = list()
        for i in range(n):
            self.data.append(Elem(i, {i}, Type.VAL))

    def get(self, i):
        return self.data[i]

    def set(self, i, value):
        if isinstance(value, set):
            t = Type.VAL
        elif isinstance(value, int):
            t = Type.PTR
        self.data[i].set(value, t)

    def find_root(self, i):
        elem = self.get(i)
        if elem.type == Type.VAL:
            return (i, elem)
        elif elem.type == Type.PTR:
            j, root_elem = self.find_root(elem.value)
            self.set(i, j)
            return (j, root_elem)
        else:
            raise Unreachable

    def run(self, command):
        com, x, y = command
        if com == 0:
            self.unite(x, y)

        elif com == 1:
            if self.same(x, y):
                print(1)
            else:
                print(0)

        else:
            raise Unreachable

    def unite(self, x, y):
        i, elem_x = self.find_root(x)
        j, elem_y = self.find_root(y)
        if i != j:
            new_set = elem_x.value | elem_y.value
            self.set(i, new_set)
            self.set(j, i)

    def same(self, x, y):
        return y in self.find_root(x)[1].value


def main():
    n, q = [int(x) for x in input().split()]
    manager = SetManager(n)

    commands = list()
    for _ in range(q):
        com, x, y = [int(x) for x in input().split()]
        commands.append((com, x, y))
    
    for command in commands:
        manager.run(command)


if __name__ == "__main__":
    main()