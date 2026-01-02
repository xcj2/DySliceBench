stack = [0]
top = 0

def push(x):
    global top
    top += 1
    stack.insert(top, x)

def pop():
    global top
    top -= 1
    return stack[top+1]

def main():
    input_line = input().split(" ")
    for i in input_line:
        if i == "+":
            a = pop()
            b = pop()
            push(a+b)
        elif i == "-":
            b = pop()
            a = pop()
            push(a-b)
        elif i == "*":
            a = pop()
            b = pop()
            push(a*b)
        else:
            push(int(i))
    
    print(pop())

if __name__ == '__main__':
    main()
    

