data = input().split()

# ??????????????????????????????????£?
# n : ????????????????????????
# S : ????????????
n = 1000
S = [0 for i in range(n)]

def isEmpty():
    global top
    if (top == 0):
        return True
    else:
        return False

def isFull():
    global top, n
    return top > n-1

def push(S, x):
    global top
    if isFull():
        print('error: overflow')
        return False
    top += 1
    S[top] = x

def pop(S):
    global top
    if isEmpty():
        print('error: underflow')
        return False
    top -= 1
    return S[top+1]

top = 0

for e in data:


    if e.isdigit():
        push(S, e)
    else:
        a = int(pop(S))
        b = int(pop(S))

        if e == '+':
            push(S, b + a)
        elif e == '-':
            push(S, b - a)
        elif e == '*':
            push(S, b * a)
        else:
            print('error: operand')


print(S[top])