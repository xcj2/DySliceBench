# coding: UTF-8
#@document_it
def document_it(func):
    def new_function(*args,**kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Kewword arguments:', kwargs)
        result = func(*args,**kwargs)
        print('Result:', result)
        return result
    return new_function

def divide(n):
    import math
    m = math.ceil(math.sqrt(n))
    d = 2
    while d <= m:
        if n % d == 0:
            return d,n//d
        d += 1
    return n,1

def exe():
    string = input()
    n = int(string)
    factors=[]
    d,a = divide(n)
    factors.append(str(d))
    while a != 1:
        d,a = divide(a)
        factors.append(str(d))
    ans = string + ': ' + ' '.join(factors)
    print(ans)
 
if __name__ == '__main__':
    exe()

