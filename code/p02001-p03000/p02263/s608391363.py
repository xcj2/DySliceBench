# Algorithms and Data Structures 1
# Stack
# Name: Ryuya Asada
# ID: s1260064


class Stack():
    def __init__(self, size):
        self.__top = 0
        self.__stack = [int] * (size+1)

    def isEmpty(self) -> bool:
        return self.__top == 0

    def isFull(self) -> bool:
        return self.__top >= len(self.__stack)-1

    def push(self, x):
        if self.isFull():
            print("Overflow!")
        
        self.__top += 1
        self.__stack[self.__top] = x

    def pop(self):
        if self.isEmpty():
            print("Underflow!")

        self.__top -= 1
        return self.__stack[self.__top+1]


def main():
    s = Stack(100)
    operation = input().split(" ")
    for o in operation:
        if o == '+':
            a, b = s.pop(), s.pop()
            s.push(a + b)
        elif o == '-':
            b, a = s.pop(), s.pop()
            s.push(a - b)
        elif o == '*':
            a, b = s.pop(), s.pop()
            s.push(a * b)
        else:
            s.push(int(o))

    print(s.pop())


if __name__ == "__main__":
    main()

