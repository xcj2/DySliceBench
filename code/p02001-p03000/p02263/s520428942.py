class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop(-1)

def calc(array):
    stack = Stack()
    for s in array:
        if s.isdigit():
            stack.push(int(s))
        else:
            o2 = stack.pop()
            o1 = stack.pop()
            ans = 0
            if s == '+':
                ans = o1 + o2
            elif s == '-':
                ans = o1 - o2
            elif s == '*':
                ans = o1 * o2
            elif s == '/':
                ans = o1 / o2
            stack.push(ans)
    return stack.pop()


def main():
    in_arr = input().split()
    print(calc(in_arr))

if __name__ == '__main__':
    main()