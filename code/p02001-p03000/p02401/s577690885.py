while True:
    line = input().split()
    a = int(line[0])
    op = line[1]
    b = int(line[2])
    
    def add(a, b):
        add = a + b
        return add
    def sub(a, b):
        sub = a - b
        return sub
    def mul(a, b):
        mul = a * b
        return mul
    def div(a, b):
        div = a // b
        return div
    
    if op == '+':
        print(add(a, b))
    elif op == '-':
        print(sub(a, b))
    elif op == '*':
        print(mul(a, b))
    elif op == '/':
        print(div(a, b))
    else:
        break
        
