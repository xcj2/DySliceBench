
def add(Stack):
    tmp = Stack[-1] + Stack[-2]
    Stack.pop(-1)
    Stack.pop(-1)
    Stack.append(tmp)
    return Stack

def subtract(Stack):
    tmp = Stack[-2] - Stack[-1]
    Stack.pop(-1)
    Stack.pop(-1)
    Stack.append(tmp)
    return Stack

def multiple(Stack):
    tmp = Stack[-1] * Stack[-2]
    Stack.pop(-1)
    Stack.pop(-1)
    Stack.append(tmp)
    return Stack

A = input().split()
Stack = []

for i in range(len(A)):
    if A[i] == '+':
        add(Stack)
    elif A[i] == '-':
        subtract(Stack)
    elif A[i] == '*':
        multiple(Stack)
    else:
        Stack.append(int(A[i]))

print(str(Stack[0]))