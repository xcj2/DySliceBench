import functools
numbers = list(input())

expressions = set()

def subSum(currentIdx, expr):
    global expressions
    
    if currentIdx == 0:
        expressions.add(convertToString(expr))
        return

    next_expr1 = expr[:]
    next_expr2 = expr[:]
    next_expr2.insert(currentIdx, '+')

    subSum(currentIdx-1, next_expr1)
    subSum(currentIdx-1, next_expr2)

def convertToString(expr):
    ex = str(functools.reduce(lambda t, x: t + x, expr))
    return ex

def culc(expr):
    return sum(list(map(int, expr.split('+'))))

subSum(len(numbers) - 1, numbers)



print(sum(list(map(culc, list(map(str, expressions))))))