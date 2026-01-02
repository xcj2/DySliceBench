class Stack():
    def __init__(self):
        self.top = -1
        self.lists = []
    def push(self,x):
        self.top += 1
        self.lists.append(0)
        self.lists[self.top] = x
    def pop(self):
        if self.top >= 0:
            self.top -= 1
            return self.lists[self.top+1]
        else :
            print("Error")
def main():
    input_list = [i for i in input().split()]
    stack = Stack()
    for i in range(len(input_list)):
        if input_list[i] == '+':
            number_1 = stack.pop()
            number_2 = stack.pop()
            stack.push(number_2+number_1)
        elif input_list[i] == '-':
            number_1 = stack.pop()
            number_2 = stack.pop()
            stack.push(number_2-number_1)
        elif input_list[i] == '*':
            number_1 = stack.pop()
            number_2 = stack.pop()
            stack.push(number_2 * number_1)
        else:
            stack.push(int(input_list[i]))
    print(stack.lists[stack.top])
if __name__ == "__main__":
    main()
