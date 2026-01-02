import sys
#from me.io import dup_file_stdin

def prec(op):
    if op in "+-":return 1
    if op in "*/":return 2
    raise NotImplementedError()
    
def postFix(expr):
    stack = []
    operators = []
    num = 0
    isdigit = False
    for ch in expr:
        if ch.isdigit():
            isdigit = True
            num*=10
            num+=int(ch)
            continue
        else :
            if isdigit:
                stack.append(num)
                num = 0
            isdigit = False
            
            if ch == ')':
                while len(operators) > 0:
                    op = operators.pop()
                    if op == '(':
                        break
                    else:
                        stack.append(op)
                else:
                    raise ValueError
            elif ch == '(':
                operators.append(ch)
            else:
                while len(operators) > 0 and operators[-1]!='(' and prec(operators[-1]) >= prec(ch):
                    stack.append(operators.pop())
                operators.append(ch)
    if isdigit:
        stack.append(num)
    for op in operators[::-1]:
        if op not in "()":
            stack.append(op)
    return stack
        
def evaluate(stack):
    op = stack.pop()
    if type(op) is int:
        return op;
    else:
        b = evaluate(stack);
        a = evaluate(stack);
        return int(eval(str(a)+op+str(b)))

#@dup_file_stdin
def solve():
    for _ in range(int(sys.stdin.readline())):
        expr = sys.stdin.readline()[:-1].strip("=")
        print(evaluate(postFix(expr)))
        
solve()