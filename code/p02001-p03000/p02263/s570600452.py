from typing import List, Union


class Stack():
    def __init__(self):
        self.top = 0
        self.max = 200
        self.lst = [None] * self.max

    def is_empty(self) -> bool:
        if self.top == 0:
            return True
        else:
            return False

    def is_full(self) -> bool:
        if self.top >= self.max - 1:
            return True
        else:
            return False

    def push(self, x: int) -> bool:
        if self.is_full() == True:
            print("ERROR: OVERFLOW")
            return False
        self.top += 1
        self.lst[self.top] = x
        return True

    def pop(self) -> Union[bool, int]:
        if self.is_empty() == True:
            print("ERROR: UNDERFLOW")
            return False
        self.top -= 1
        return self.lst[self.top + 1]


def main():
    lst: List = list(input().split())
    S = Stack()

    for char in lst:
        if char == "+":
            b = S.pop()
            a = S.pop()
            S.push(a + b)
        elif char == "-":
            b = S.pop()
            a = S.pop()
            S.push(a - b)
        elif char == "*":
            b = S.pop()
            a = S.pop()
            S.push(a * b)
        else:
            S.push(int(char))

    print(S.lst[S.top])


if __name__ == "__main__":
    main()

