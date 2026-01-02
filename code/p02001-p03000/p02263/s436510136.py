def stack():
    A = list(input().split())
    lst = []
    
    def add(a, b):
        return b + a
    
    def sub(a, b):
        return b - a
        
    def mul(a, b):
        return b * a
    
    def div(a, b):
        return b / a
        
    def calc(lst, f):
        return lst.append(f(lst.pop(), lst.pop()))
    
    for i in A:
        if i == '+':
            calc(lst, add)
        elif i == '-':
            calc(lst, sub)
        elif i == '*':
            calc(lst, mul)
        elif i == '/':
            calc(lst, div)
        else: 
            lst.append(int(i))
    
    print(*lst)
    
stack()