class Stack():
    def __init__(self):
        self.stack = list()

    def _is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if self._is_empty():
            print('empty')
            return None
        return self.stack.pop(-1)

    def __len__(self):
        return len(self.stack)


def main():
    sentense = input().split(' ')
    stack = Stack()
    for chr in sentense:
        if chr in ['+', '-', '*']:
            b = stack.pop()
            a = stack.pop()
            if chr == '+':
                stack.push(a+b)
            elif chr == '-':
                stack.push(a-b)
            else:
                stack.push(a*b)
        else:
            stack.push(int(chr))
    print(stack.pop())


if __name__ == "__main__":
    main()

