class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        result = self.stack[-1]
        del self.stack[-1]
        return result
    
def main():
    formula = input().split()
    stack = Stack()
    operator_list = ["+", "-", "*"] #演算子リスト
    a = 0 #popした値のtemp
    b = 0 #popした値のtemp

    for i in range(len(formula)):
        if formula[i] in operator_list:
            a = stack.pop()
            b = stack.pop()
            ans = eval(str(b) + str(formula[i]) + str(a))
            stack.push(ans)
        else:
            stack.push(formula[i])

    print(stack.pop())
        


if __name__ == "__main__":
    main()
