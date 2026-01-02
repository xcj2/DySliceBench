import sys
P = list(map(str, input().split()))
MAX = len(P)
S = [0] * MAX

def initialize():
    top = 0
    return top

def isEmpty():
    return top == 0

def isFull():
    return top >= MAX - 1

def push(x, top):
    if isFull():
        print('Error')
        sys.exit()
    top += 1
    S[top] = x
    return top

def pop(top):
    if isEmpty():
        print('Error')
        sys.exit()
    top -= 1
    return top, S[top + 1]

top = initialize()
for i in range(len(P)):
    if P[i].isdecimal():
        top = push(int(P[i]), top)
    elif P[i] == '+':
        top, n1 = pop(top)
        top, n2 = pop(top)
        top = push(n2 + n1, top)
    elif P[i] == '-':
        top, n1 = pop(top)
        top, n2 = pop(top)
        top = push(n2 - n1, top)
    elif P[i] == '*':
        top, n1 = pop(top)
        top, n2 = pop(top)
        top = push(n2 * n1, top)
print(S[top])
