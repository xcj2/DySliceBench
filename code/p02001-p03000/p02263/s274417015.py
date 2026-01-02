stack = [0]*1000
top = 0

def push(x):
    global stack
    global top

    top += 1
    stack[top] = x

def pop():
    global top
    global stack

    top -= 1
    return(stack[ top + 1 ])

def main():
    global stack
    global top
    a = 0
    b = 0

    A = list(input().split())

    for i in range(len(A)):
        if A[i] not in ['+','-','*']:
            push(int(A[i]))
        elif A[i] == '+':
            a = pop()
            b = pop()
            push(b+a)
        elif A[i] == '-':
            a = pop()
            b = pop()
            push(b-a)
        elif A[i] == '*':
            a = pop()
            b = pop()
            push(b*a)

    return stack[1]

print(main())

