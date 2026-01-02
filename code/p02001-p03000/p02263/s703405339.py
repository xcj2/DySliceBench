def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b

ls=input().split()

stack=[]

i = 0
while i < len(ls):
    if ls[i] == '+':
        stack.append(add(stack[-2],stack[-1]))
        stack.pop(-3)
        stack.pop(-2)
    elif ls[i] == '-':
        stack.append(sub(stack[-2],stack[-1]))
        stack.pop(-3)
        stack.pop(-2)
    elif ls[i] == '*':
        stack.append(mul(stack[-2],stack[-1]))
        stack.pop(-3)
        stack.pop(-2)
    else:
        stack.append(int(ls[i]))
    i+=1
print(stack[-1])
