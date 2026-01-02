def getInput():
    a = input().split()
    return a

def convNum(s):
    if s.isdigit():
        return int(s)
    else:
        return s
def initArr(len_a):
    return 0, [0 for i in range(len_a+1)]

def initTop():
    return 0

def isEmpty(top):
    return top == 0
    
def isFull(top, len_a):
    return top >= len_a-1

def pop(top, a):
    if isEmpty(top):
        print("Err: Empty")
    val = a[top]
    top -= 1
    return top, val

def push(top, a, val):
    if isFull(top, len(a)):
        print("Err: Full")
    top += 1
    a[top] = val
    return top

a = getInput()
a = [convNum(i) for i in a]

top, s = initArr(len(a))
for i in range(len(a)):
    top = push(top, s, a[i])
    if type(a[i]) == str:
        top, val = pop(top, s)
        top, val_b = pop(top, s)
        top, val_a = pop(top, s)
        if val == "+":
            top = push(top, s, val_a + val_b)
        elif val == "-":
            top = push(top, s, val_a - val_b)
        elif val == "*":
            top = push(top, s, val_a * val_b)        
        else:
            print("Error: Invalid Operand")
print(s[1])
