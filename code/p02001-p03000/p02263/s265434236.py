# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A&lang=jp

class Stack(object):
    def __init__(self, num):
        self.list = []
        self.num = num
    
    def push(self, x):
        self.list.append(x)

    def pop(self):
        return self.list.pop(-1)
    
    def isEmpty(self):
        return len(self.list) == 0
    
    def isFull(self):
        return self.num <= len(self.list)



def main():
    li = list(input().split(' '))

    stack = Stack(999999)
    OPERANDS = ['+', '-', '*']
    
    for x in li:
        if not (x in OPERANDS):
            stack.push(int(x))
        else:
            b = stack.pop()
            a = stack.pop()

            if x == '+':
                stack.push(a + b)
            elif x == '-':
                stack.push(a - b)
            elif x == '*':
                stack.push(a * b)
        # print(stack.list)

    ans = stack.pop()
    print(ans)


        

main()
