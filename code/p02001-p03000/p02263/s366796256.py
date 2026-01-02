class Stack(object):
    def __init__(self, _max):
        if type(_max) == int:
            self._array = [None for i in range(0, _max)]
            self._next = 0

    def push(self, value):
        if self.isFull():
            raise IndexError
        self._array[self._next] = value
        self._next += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError
        self._next -= 1
        value = self._array[self._next]
        self._array[self._next] = None
        return value

    def isEmpty(self):
        return self._next <= 0

    def isFull(self):
        return self._next >= len(self._array)


def calculator(exp):
    stack = Stack(100)
    ope = ["+", "-", "*"]
    for item in exp:
        if item in ope:
            val1 = stack.pop()
            val2 = stack.pop()
            if item == "+":
                stack.push(val2 + val1)
            elif item == "-":
                stack.push(val2 - val1)
            elif item == "*":
                stack.push(val2 * val1)
            else:
                raise ValueError
        else:
            stack.push(int(item))
    return stack.pop()


if __name__ == "__main__":
    exp = input().split()
    print(calculator(exp))