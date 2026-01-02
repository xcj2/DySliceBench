import operator
operator = {"+": operator.add, "-": operator.sub, "*": operator.mul}

def initialize():
    top = 0

def empty_or_not():
    return top == 0

def full_or_not():
    return top >= len(s) - 1

def push(x):
    global top
    if full_or_not():
        raise ValueError("Error: stack is full!")
    top += 1
    s[top] = x

def pop():
    global top
    if empty_or_not():
        raise ValueError("Error: stack is empty!")
    top -= 1
    return s[top+1]



s = [None] * 10**3
top = 0

rpn = list(input().split())

for i in range(len(rpn)):
    if rpn[i] == "+" or rpn[i] == "-" or rpn[i] == "*":
        b = int(pop())
        a = int(pop())
        
        a_ops_b = operator[rpn[i]](a, b)
        #print(f"ops: {a} {rpn[i]} {b} = {a_ops_b}")
        push(a_ops_b)
        #print(f"top: {top}")
        #print(s)
    else:
        #print(f"push: {rpn[i]}")
        push(rpn[i])
        #print(f"top: {top}")
        #print(s)
        
print(s[top])


    
