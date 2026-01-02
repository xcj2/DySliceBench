class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop(-1)

    @property
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

def main():
    s = input()
    stack_grad = Stack()
    stack_vol = Stack()
    sum_vol = 0

    for i, c in enumerate(s):
        if c == '\\':
            stack_grad.push(i)
        elif c == '/':
            if not stack_grad.isEmpty:
                previ = stack_grad.pop()
                vol = i - previ
                sum_vol += vol
                while not stack_vol.isEmpty:
                    tpl = stack_vol.pop()
                    if previ < tpl[0]:
                        vol += tpl[1]
                    else:
                        stack_vol.push(tpl)
                        break
                stack_vol.push((previ, vol))

    print(sum_vol)
    stack_vol.stack.reverse()
    out = str(len(stack_vol.stack))
    while not stack_vol.isEmpty:
        out += ' {}'.format(stack_vol.pop()[1])
    print(out)


if __name__ == '__main__':
    main()