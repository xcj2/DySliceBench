# encoding: "utf-8"

class Unreachable(Exception):
    pass


class SetManager:
    def __init__(self, n):
        self.data = list()
        for i in range(n):
            self.data.append((i, {i}))

    def ref(self, i):
        return self.data[i][1]

    def set(self, i, value):
        self.data[i] = (i, value)

    def find_set(self, i):
        value = self.ref(i)
        if isinstance(value, set):
            return self.data[i]
        elif isinstance(value, int):
            result = self.find_set(value)
            self.set(i, result[0])
            return result
        else:
            raise Unreachable

    def run(self, command):
        com, x, y = command
        if com == 0:
            # unite
            i, setx = self.find_set(x)
            j, sety = self.find_set(y)
            if i != j:
                new_set = setx | sety
                self.set(i, new_set)
                self.set(j, i)

        elif com == 1:
            # same
            if y in self.find_set(x)[1]:
                print(1)
            else:
                print(0)
        else:
            raise Unreachable

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