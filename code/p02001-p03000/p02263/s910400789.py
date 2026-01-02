S =[]
S.append(0)
top = 0
MAX = 1000
t = 0

def initialize():
    top = 0

def isEmpty():
    return top == 0

def isFull():
    return top >= MAX - 1

def push(x):
    global top
    if isFull():
        print("error")
    top += 1
    S.append(x)

def pop():
    global top
    global t
    t = 0
    if isEmpty():
        print("error")
    top -= 1
    t = S[top + 1]
    del S[top + 1]
    return t

L = input().split()

for i in range(len(L)):
    if L[i] == "+":
        push(int(pop()) + int(pop()))
    elif L[i] == "-":
        push(-(int(pop()) - int(pop())))
    elif L[i] == "*":
        push(int(pop()) * int(pop()))
    else:
        push(L[i])
print(S[top])
