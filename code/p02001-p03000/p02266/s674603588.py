def main():
    inputs = str(input())
    stack = []
    pond = [Pond(-1, 0, 0)]

    for i, string in enumerate(inputs):
        if string == "\\":
            stack.append(i)
        elif string == "/":
            try:
                down = stack.pop()
            except  IndexError as err:
                continue
            pond.append(Pond(down, i, i-down))
            while len(pond) > 1:
                newPond = pond.pop()
                prevPond = pond.pop()
                if prevPond.includedBy(newPond):
                    pond.append(prevPond.merge(newPond))
                else:
                    break
            pond.append(prevPond)
            pond.append(newPond)

    printPonds(pond)

def printPonds(pond):
    size = 0
    eachSize = []
    for p in pond:
        size += p.size
        eachSize.append(p.size)
    eachSize[0] = len(pond)-1
    print(size)
    print(*eachSize)

class Pond:
    def __init__(self, x1, x2, size):
        self.x1 = x1
        self.x2 = x2
        self.size = size

    def merge(self, newPond):
        self.x1 = newPond.x1
        self.x2 = newPond.x2
        self.size += newPond.size
        return self

    def includedBy(self, newPond):
        return self.x1 >= newPond.x1 and self.x2 <= newPond.x2

if __name__ == "__main__":
    main()
